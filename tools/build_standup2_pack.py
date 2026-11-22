"""Build the Stand Up 2 Design Book PDF, Markdown notes and KNIME copy.

GenAI prompt summary: package existing evidence for Huy's 23 November stand-up.
Preserve source data and node settings, distinguish static checks from desktop
execution, and preserve Markdown presenter notes without inventing results.
Requires ReportLab, Pillow and Inkscape. The production website is unchanged.
"""

import argparse
import copy
import csv
import hashlib
from html import escape
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import textwrap
import xml.etree.ElementTree as ET
import zipfile

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, Image, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
TEAM = "Gr_01_StandUp2"
INK, NAVY, MUTED = "#142b3d", "#244d68", "#51616a"
NS = {"k": "http://www.knime.org/2008/09/XMLConfig"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def package_knime(out):
    source = ROOT / "knime/COS30045_Project.knwf"
    target = out / (TEAM + ".knwf")
    with zipfile.ZipFile(source) as archive:
        assert archive.testzip() is None, "Input KNIME archive is corrupt"
        old_root = archive.namelist()[0].split("/")[0]
        original = {i.filename: archive.read(i) for i in archive.infolist()}
        workflow = ET.fromstring(original[old_root + "/workflow.knime"])
        nodes = workflow.find("k:config[@key='nodes']", NS)
        node_count = len(list(nodes))
        assert node_count == 10
        assert workflow.find("k:entry[@key='state']", NS).get("value") == "EXECUTED"
        assert old_root + "/.savedWithData" in original
        replacements = {
            "Individual project: Nguyen Huyen Minh Nhat.": "Gr_01 team project: Nhat and Huy.",
            "individual KNIME workflow": "team KNIME workflow",
        }
        changed = []
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as result:
            for info in archive.infolist():
                data = original[info.filename]
                rel = info.filename[len(old_root) + 1:]
                if rel in {"workflow.knime", "workflow.svg"}:
                    text = data.decode("utf-8")
                    for a, b in replacements.items():
                        text = text.replace(a, b)
                    data = text.encode("utf-8")
                    if data != original[info.filename]:
                        changed.append(rel)
                new_info = copy.copy(info)
                new_info.filename = TEAM + "/" + rel
                result.writestr(new_info, data)
    with zipfile.ZipFile(target) as result:
        assert result.testzip() is None
        assert len(result.namelist()) == len(original)
        for name, data in original.items():
            rel = name[len(old_root) + 1:]
            new = result.read(TEAM + "/" + rel)
            if rel not in changed:
                assert new == data, rel
            if rel.endswith((".xml", ".knime", ".meta")):
                ET.fromstring(new)
        raw = result.read(TEAM + "/data/hospitalisation_injury_publication_sep2023.xlsx")
        assert sha(raw) == sha((ROOT / "data/raw/hospitalisation_injury_publication_sep2023.xlsx").read_bytes())
        exports = {}
        for filename, expected in [("annual_totals.csv", 11), ("road_user_by_year.csv", 132), ("age_sex_by_road_user.csv", 1683)]:
            data = result.read(TEAM + "/data/processed/" + filename)
            rows = list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))
            assert len(rows) == expected
            assert data == (ROOT / "data/processed" / filename).read_bytes()
            exports[filename] = {"rows": len(rows), "sha256": sha(data)}
        reader = ET.fromstring(result.read(TEAM + "/Excel Reader (#1)/settings.xml"))
        assert any(e.get("key") == "file_system_specifier" and e.get("value") == "knime.workflow.data" for e in reader.iter())
        assert any(e.get("key") == "path" and e.get("value") == "hospitalisation_injury_publication_sep2023.xlsx" for e in reader.iter())
        for filename in ["CSV Writer (#6)", "CSV Writer (#8)", "CSV Writer (#10)"]:
            xml = result.read(TEAM + "/" + filename + "/settings.xml")
            assert b"knime.workflow" in xml
        svg = result.read(TEAM + "/workflow.svg")
        readable_svg = "\n".join(line.rstrip() for line in svg.decode("utf-8").splitlines()) + "\n"
        (ROOT / "docs/StandUp_02/current_workflow.svg").write_text(readable_svg)
    report = {
        "status": "PASS_STATIC_PACKAGE_CHECKS", "archive": target.name,
        "source_archive": str(source.relative_to(ROOT)), "root": TEAM,
        "nodes": node_count, "saved_state": "EXECUTED", "saved_with_data": True,
        "source_workbook_sha256": sha(raw), "exports": exports,
        "modified_entry_contents": changed,
        "unchanged": "Raw workbook, CSV exports, node settings and saved execution data",
        "desktop_import_and_execution": "PENDING_ON_PRESENTATION_LAPTOP",
    }
    (out / "KNIME_package_check.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def fonts():
    root = Path("/usr/share/fonts/truetype/dejavu")
    for name, filename in [("Body", "DejaVuSans.ttf"), ("BodyBold", "DejaVuSans-Bold.ttf"), ("BodyItalic", "DejaVuSans-Oblique.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(root / filename)))
    pdfmetrics.registerFontFamily("Body", normal="Body", bold="BodyBold", italic="BodyItalic")


def inline(text):
    text = escape(text)
    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)", lambda m: m.group(1), text)
    text = re.sub(r"`([^`]+)`", r'<font name="Body">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    return text


def image_flowable(source, assets):
    if source.suffix == ".svg":
        if source.name == "current_workflow.svg":
            # Inkscape omits HTML foreignObject labels from KNIME's saved SVG.
            # Render the saved labels as native SVG text in the PDF copy only.
            ns = "http://www.w3.org/2000/svg"
            root = ET.fromstring(source.read_bytes())
            parents = {child: parent for parent in root.iter() for child in parent}
            for item in list(root.iter("{" + ns + "}foreignObject")):
                x, y = float(item.get("x", 0)), float(item.get("y", 0))
                width = float(item.get("width", 200))
                raw = ET.tostring(item, encoding="unicode")
                match = re.search(r"font-size:\s*([0-9.]+)px", raw)
                size = float(match[1]) if match else 16
                label = "".join(item.itertext()).strip()
                group = ET.Element("{" + ns + "}g")
                lines = []
                for line in label.splitlines():
                    lines.extend(textwrap.wrap(line.strip(), max(8, int(width / (size * .54))), break_long_words=False) or [""])
                for i, line in enumerate(lines):
                    t = ET.SubElement(group, "{" + ns + "}text", {"x": str(x), "y": str(y + size + i * size * 1.2),
                                     "font-size": str(size), "font-family": "DejaVu Sans", "fill": INK})
                    t.text = line
                parent = parents[item]; at = list(parent).index(item)
                parent.remove(item); parent.insert(at, group)
            converted = assets / "workflow_print.svg"
            ET.ElementTree(root).write(converted, encoding="utf-8", xml_declaration=True)
            source = converted
        target = assets / (source.stem + ".png")
        r = subprocess.run(["inkscape", str(source), "--export-type=png", "--export-width=2000", "--export-filename=" + str(target)], capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError("SVG rendering failed for " + source.name + ": " + r.stderr[:300])
    else:
        target = source
    with PILImage.open(target) as im:
        w, h = im.size
        # Two columns preserve readable text in the long mobile wireframe.
        if source.name == "wireframe_mobile.svg":
            middle = h // 2
            left, right = im.crop((0, 0, w, middle)), im.crop((0, middle, w, h))
            canvas = PILImage.new("RGB", (w * 2 + 40, max(left.height, right.height)), "white")
            canvas.paste(left, (0, 0)); canvas.paste(right, (w + 40, 0))
            target = assets / "mobile_two_columns.png"; canvas.save(target)
            w, h = canvas.size
    width = A4[0] - 92
    scale = min(width / w, 355 / h)
    return Image(str(target), width=w * scale, height=h * scale)


def build_pdf(source, target, assets, label):
    styles = getSampleStyleSheet()
    style = {
        "body": ParagraphStyle("Body", fontName="Body", fontSize=9.5, leading=13.6, textColor=colors.HexColor(INK), spaceAfter=7),
        "title": ParagraphStyle("Title", fontName="BodyBold", fontSize=25, leading=30, textColor=colors.HexColor(INK), spaceAfter=18),
        "h2": ParagraphStyle("H2", fontName="BodyBold", fontSize=15, leading=20, textColor=colors.HexColor(NAVY), spaceBefore=15, spaceAfter=9, keepWithNext=True),
        "h3": ParagraphStyle("H3", fontName="BodyBold", fontSize=11.5, leading=16, textColor=colors.HexColor(INK), spaceBefore=12, spaceAfter=7, keepWithNext=True),
        "h4": ParagraphStyle("H4", fontName="BodyBold", fontSize=10, leading=14, textColor=colors.HexColor(INK), spaceBefore=10, spaceAfter=6, keepWithNext=True),
        "cell": ParagraphStyle("Cell", fontName="Body", fontSize=8.3, leading=11.5, textColor=colors.HexColor(INK)),
        "caption": ParagraphStyle("Caption", fontName="BodyItalic", fontSize=8, leading=11, textColor=colors.HexColor(MUTED), spaceAfter=10),
    }
    doc = BaseDocTemplate(str(target), pagesize=A4, leftMargin=46, rightMargin=46, topMargin=45, bottomMargin=45,
                          title=source.stem.replace("_", " "), author="Nguyen Huyen Minh Nhat and Le Tuan Huy")
    def footer(canvas, document):
        canvas.setFont("Body", 7.5); canvas.setFillColor(colors.HexColor(MUTED))
        canvas.drawString(46, 25, label)
        canvas.drawRightString(A4[0] - 46, 25, str(document.page))
    doc.addPageTemplates(PageTemplate(id="main", frames=[Frame(46, 45, A4[0]-92, A4[1]-90, leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0)], onPage=footer))
    lines = source.read_text().splitlines()
    story = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1; continue
        image = re.fullmatch(r"!\[([^]]*)\]\(([^)]+)\)", line)
        if image:
            story.append(image_flowable((source.parent / image[2]).resolve(), assets))
            story.append(Paragraph(inline(image[1]), style["caption"]))
        elif line.startswith("|"):
            table = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    table.append([Paragraph(inline(c), style["cell"]) for c in cells])
                i += 1
            n = len(table[0]); width = A4[0] - 92
            if n == 2:
                widths = [width * .31, width * .69]
            else:
                widths = [width / n] * n
            t = Table(table, colWidths=widths, repeatRows=1, hAlign="LEFT")
            t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eaf0f3")),
                                   ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                                   ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                                   ("LINEBELOW", (0, 0), (-1, 0), .5, colors.HexColor("#9da9b0")),
                                   ("LINEBELOW", (0, 1), (-1, -1), .25, colors.HexColor("#d7dcd9"))]))
            story.extend([t, Spacer(1, 9)])
            continue
        elif line.startswith("#"):
            depth = len(line) - len(line.lstrip("#"))
            content = line[depth:].strip()
            if content == "3 Visualisation Design": story.append(PageBreak())
            story.append(Paragraph(inline(content), style[{1:"title",2:"h2",3:"h3"}.get(depth,"h4")]))
        elif line.startswith("- "):
            story.append(Paragraph(inline(line), style["body"]))
        elif re.match(r"\d+\.\s", line):
            story.append(Paragraph(inline(line), style["body"]))
        else:
            paragraph = [line]
            while i + 1 < len(lines) and lines[i+1].strip() and not lines[i+1].lstrip().startswith(("#", "|", "- ", "![")) and not re.match(r"\d+\.\s", lines[i+1].lstrip()):
                i += 1; paragraph.append(lines[i].strip())
            story.append(KeepTogether([Paragraph(inline(" ".join(paragraph)), style["body"])]))
        i += 1
    doc.build(story)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve(); out.mkdir(parents=True, exist_ok=True)
    assets = out / "render_assets"; assets.mkdir(exist_ok=True)
    report = package_knime(out)
    fonts()
    build_pdf(ROOT / "docs/design_book/Gr_01_StandUp2_Draft.md", out / "Gr_01_StandUp2_Design_Book.pdf", assets, "Gr_01 - Stand Up 2 Design Book draft - 22 November 2026")
    notes_source = ROOT / "docs/StandUp_02/Gr_01_StandUp2_Huy_Notes.md"
    shutil.copy2(notes_source, out / notes_source.name)
    notes = notes_source.read_text()
    speech = []
    main_script = notes.split("## Slide 1 -", 1)[1].split("## Demo web", 1)[0]
    assert len(re.findall(r"^## Slide [2-5] -", main_script, re.M)) == 4
    for line in main_script.splitlines():
        if line.startswith("| ") and not line.startswith(("| Say", "| ---")):
            speech.append(line.split("|")[1].strip())
    words = len(re.findall(r"\S+", " ".join(speech)))
    print(json.dumps({"knime": report["status"], "spoken_words": words,
                      "presentation": "https://chatgpt.com/space/page_ea183a7225cc8191ab4a21aee0030aea",
                      "outputs": [p.name for p in sorted(out.iterdir()) if p.is_file()]}, indent=2))


if __name__ == "__main__":
    main()
