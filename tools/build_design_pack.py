"""Build the Week 11 design evidence from the committed analysis CSVs.

GenAI prompt summary: turn the verified storyboard into labelled, reproducible
chart alternatives and desktop/mobile wireframes. Keep proposed UI distinct from
working D3 code, and preserve categories, denominators and source limitations.
Requires Matplotlib and NumPy for these static design assets, not for the website.
"""

import csv
from html import escape
from pathlib import Path
import textwrap

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgb
from matplotlib.ticker import FuncFormatter
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/design"
NAVY, RUST, INK, MUTED = "#244d68", "#a74527", "#142b3d", "#51616a"
AGES = ["0-7", "8-16", "17-25", "26-39", "40-64", "65-74", "75+", "Missing"]


def luminance(colour):
    rgb = to_rgb(colour)
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    return sum(c * weight for c, weight in zip(linear, [.2126, .7152, .0722]))


def cell_text(colour):
    background = luminance(colour)
    for foreground in [INK, "white", "black"]:
        light, dark = sorted([background, luminance(foreground)], reverse=True)
        if (light + .05) / (dark + .05) >= 4.5:
            return foreground
    raise ValueError("No readable cell text colour")


def rows(name):
    with (ROOT / "data/analysis" / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def write(name, content):
    (OUT / name).write_text("\n".join(line.rstrip() for line in content.splitlines()) + "\n", encoding="utf-8")


def save(fig, name):
    fig.savefig(OUT / name, format="svg", bbox_inches="tight", metadata={"Date": None})
    plt.close(fig)
    write(name, (OUT / name).read_text(encoding="utf-8"))


def svg(title, width, height, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
            '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#142b3d} '
            '.small{font-size:15px}.label{font-size:19px;font-weight:700}</style>'
            f'<rect width="{width}" height="{height}" fill="#f8f7f3"/>{body}</svg>')


def label(x, y, value, size=18, weight="normal"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}">{escape(value)}</text>'


def box(x, y, w, h, title, lines=()):
    body = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="white" stroke="#51616a"/>'
    body += label(x + 16, y + 29, title, 18, "bold")
    for i, line in enumerate(lines):
        body += label(x + 16, y + 55 + i * 23, line, 16)
    return body


def wireframes():
    body = label(28, 38, "DESKTOP / planned 1440 px layout", 24, "bold")
    body += box(28, 62, 1064, 65, "Gr_01 / Beyond the Total", ["Anchor navigation: Compare | Events | Ages | Method   /   Reset story"])
    body += box(28, 145, 1064, 120, "01 / One decline, different directions", [
        "2019-2020: national -4.8%; cyclists +14.1%. Counts are not exposure-adjusted risk.",
        "Brief national trend 2011-2021 below the opening; mark the 2012 and 2017 breaks."])
    body += box(28, 283, 292, 188, "02 / Compare", ["Question and short finding", "Year A: 2019 / Year B: 2020", "Select road user: cyclist", "All 12 road users retained", "Year colours stay fixed"])
    body += box(340, 283, 752, 188, "Dumbbell / shared count axis starts at zero", ["2019 circle / 2020 diamond; count and signed-change labels", "Selected row: outline and bold label; no colour reassignment", "Exact values available by focus and in the chapter table"])
    body += box(28, 489, 1064, 82, "Detail controls / separate from the comparison years", ["Detail year: 2021 / Road user: Pedal cyclist / Always show both in the heading"])
    body += box(28, 588, 292, 151, "03 / Event classifications", ["What was recorded?", "3,705 / 8,163 = 45.4%", "Non-collision is a category", "Links do not identify fault"])
    body += box(340, 588, 752, 151, "Two-column Sankey / one selected group", ["Road user -> recorded counterparty; link width = Hospitalisations", "Non-collision and unspecified stay separate; full category table", "Candidate matrix if between-group comparison is the main task"])
    body += box(28, 757, 292, 151, "04 / Age profiles", ["Compare composition", "2021 / all source sexes", "Unequal age-band widths", "Unknown stays in denominator"])
    body += box(340, 757, 752, 151, "Heatmap / all 12 groups x 8 age categories", ["Default: within-road-user % / alternative: count", "Sequential scale, exact labels, selected row outline", "Legend and table update with the metric"])
    body += box(28, 926, 1064, 104, "05 / Takeaway, exact values and method", ["A table below each chapter; source/release, denominator and recording-break notes", "Conclude with the three observations. Do not imply 2021 profiles explain a 2020 change."])
    write("wireframe_desktop.svg", svg("Desktop website wireframe with reading order, charts and controls", 1120, 1058, body))
    body = label(20, 35, "MOBILE / planned 375 px layout", 20, "bold")
    blocks = [
        ("Header and anchors", ["Skip to story / chapter links wrap", "Reset restores defaults, keeps scroll"]),
        ("Opening question", ["National -4.8% / cyclist +14.1%", "2019-2020 stays visible"]),
        ("Compare controls + question", ["Year A / Year B / road user", "Native controls, full-width labels"]),
        ("Compact comparison", ["Selected group: paired count bars", "2019 / 2020 labels + signed change", "All 12 groups in table below"]),
        ("Detail year / road user", ["2021 / Pedal cyclist", "Independent of comparison years"]),
        ("Recorded event categories", ["Horizontal share bars + counts", "All categories in exact table", "Sankey replaced when too narrow"]),
        ("Age composition", ["Selected group: age bars", "Count / within-group % switch", "All groups available in table"]),
        ("Takeaway and method", ["Source, caveats and exact tables", "No page-wide sideways scroll"]),
    ]
    y = 56
    for title, lines in blocks:
        h = 65 + len(lines) * 23
        body += box(20, y, 365, h, title, lines)
        y += h + 15
    write("wireframe_mobile.svg", svg("Narrow-screen wireframe showing compact chart and table alternatives", 425, y + 10, body))


def comparison():
    source = rows("road_user_changes_2019_2020.csv")
    national = next(r for r in source if r["road_user"] == "All road users")
    groups = sorted((r for r in source if r["road_user"] != "All road users"),
                    key=lambda r: -int(r["hospitalisations_2019"]))
    assert len(groups) == 12
    assert sum(int(r["hospitalisations_2019"]) for r in groups) == int(national["hospitalisations_2019"])
    assert sum(int(r["hospitalisations_2020"]) for r in groups) == int(national["hospitalisations_2020"])
    a = np.array([int(r["hospitalisations_2019"]) for r in groups])
    b = np.array([int(r["hospitalisations_2020"]) for r in groups])
    y = np.arange(len(groups))
    fig, axes = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={"width_ratios": [1.3, 1]})
    for ax in axes:
        ax.set_yticks(y, ["\n".join(textwrap.wrap(r["road_user"], 25)) for r in groups], fontsize=10)
        ax.set_ylim(len(groups) - .4, -.6)
        ax.set_xlim(0, 16000)
        ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:,.0f}"))
        ax.set_xlabel("Hospitalisations (count)")
        ax.grid(axis="x", color="#d7dcd9", linewidth=.6)
        ax.set_axisbelow(True)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="y", length=0)
    axes[0].set_title("CHOSEN / Dumbbell\nShared positions expose direction and size", loc="left", pad=18)
    axes[0].hlines(y, a, b, color=MUTED, linewidth=2)
    axes[0].scatter(a, y, color=NAVY, marker="o", s=44, label="2019 / circle", zorder=3)
    axes[0].scatter(b, y, color=RUST, marker="D", s=40, label="2020 / diamond", zorder=3)
    for i, r in enumerate(groups):
        axes[0].text(max(a[i], b[i]) + 240, i, f'{int(r["absolute_change"]):+,}', va="center", fontsize=10)
        if r["road_user"] == "Pedal cyclist":
            axes[0].axhspan(i - .38, i + .38, facecolor="none", edgecolor=INK, linewidth=1.2)
            axes[0].get_yticklabels()[i].set_fontweight("bold")
    axes[1].set_title("ALTERNATIVE / Grouped bars\nFamiliar, but uses twice as many marks", loc="left", pad=18)
    axes[1].barh(y - .17, a, height=.31, color=NAVY, label="2019")
    axes[1].barh(y + .17, b, height=.31, color=RUST, label="2020", hatch="//")
    for ax in axes:
        ax.legend(loc="lower right", frameon=False, fontsize=10)
    fig.suptitle("02 / Did every road user follow the national decline?", x=.02, ha="left", fontsize=18)
    fig.text(.02, .025, "2019-2020 | All 12 road-user categories | National: 39,866 to 37,966 (-4.8%) | Cyclists: +1,030 (+14.1%)\nLabels on dumbbell show absolute change, not change in risk. Small groups remain visible in the table.", fontsize=11)
    fig.tight_layout(rect=(0, .08, 1, .94), w_pad=3)
    save(fig, "sketch_comparison.svg")
    return groups


def ages(groups):
    data = {(r["road_user"], r["age_group"]): int(r["hospitalisations"])
            for r in rows("age_by_road_user.csv") if r["year"] == "2021"}
    names = [r["road_user"] for r in groups]
    counts = np.array([[data.get((name, age), 0) for age in AGES] for name in names])
    with (ROOT / "data/processed/road_user_by_year.csv").open(newline="") as f:
        totals = {r["road_user"]: int(r["hospitalisations"]) for r in csv.DictReader(f) if r["year"] == "2021"}
    assert all(sum(counts[i]) == totals[name] for i, name in enumerate(names))
    shares = counts / counts.sum(axis=1)[:, None] * 100
    assert np.allclose(shares.sum(axis=1), 100)
    cyclist = names.index("Pedal cyclist")
    assert counts[cyclist, AGES.index("40-64")] == 3393
    fig, axes = plt.subplots(1, 2, figsize=(17, 8.5), gridspec_kw={"width_ratios": [1.7, 1]})
    cmap = LinearSegmentedColormap.from_list("composition", ["#f2f6f8", NAVY])
    im = axes[0].imshow(shares, cmap=cmap, vmin=0, vmax=100, aspect="auto")
    axes[0].set_xticks(range(8), [a if a != "Missing" else "Unknown" for a in AGES], fontsize=10)
    axes[0].set_yticks(range(12), ["\n".join(textwrap.wrap(n, 24)) for n in names], fontsize=10)
    for i in range(12):
        for j in range(8):
            axes[0].text(j, i, f"{shares[i, j]:.1f}", ha="center", va="center", fontsize=9,
                         color=cell_text(cmap(shares[i, j] / 100)))
    from matplotlib.patches import Rectangle
    axes[0].add_patch(Rectangle((-.5, cyclist - .5), 8, 1, fill=False, edgecolor=INK, linewidth=2))
    fig.colorbar(im, ax=axes[0], orientation="horizontal", pad=.07, fraction=.055,
                 label="Within-road-user share (%) / fixed 0-100 scale across years")
    axes[0].set_title("CHOSEN / Heatmap\nCompare age composition across all 12 groups", loc="left", pad=18)
    axes[1].barh(range(8), shares[cyclist], color=NAVY)
    axes[1].set_yticks(range(8), [a if a != "Missing" else "Unknown" for a in AGES])
    axes[1].invert_yaxis()
    axes[1].set_xlim(0, 100)
    axes[1].set_xlabel("Share within cyclists (%)")
    axes[1].set_title("ALTERNATIVE / One-group bars\nMore precise; mobile default", loc="left", pad=18)
    for j in range(8):
        axes[1].text(shares[cyclist, j] + 1.5, j, f"{shares[cyclist, j]:.1f}%", va="center", fontsize=10)
    axes[1].spines[["top", "right"]].set_visible(False)
    fig.suptitle("04 / Do road users have the same age profile?", x=.02, ha="left", fontsize=18)
    fig.text(.02, .018, "2021 | All source sex categories | % denominator: each road user's full total, including Unknown\nAge bands have unequal widths. Blank raw measures are not imputed; absent aggregate keys are zero after reconciliation. Values are composition, not age-specific risk.", fontsize=11)
    fig.tight_layout(rect=(0, .09, 1, .94), w_pad=3)
    save(fig, "sketch_age.svg")


def counterparty(groups):
    source = rows("counterparty_by_road_user.csv")
    data = {r["counterparty"]: int(r["hospitalisations"])
            for r in source
            if r["year"] == "2021" and r["road_user"] == "Pedal cyclist"}
    selected = ["Non-collision transport accident", "Other and unspecified transport accidents", "Car, pick-up truck or van"]
    bins = [(key, data[key]) for key in selected]
    bins.append(("Other recorded categories", sum(v for k, v in data.items() if k not in selected)))
    assert sum(v for _, v in bins) == 8163
    assert [v for _, v in bins] == [3705, 1854, 1575, 1029]
    scale = 350 / 8163
    source_y, target_y = 170, 122
    body = label(24, 38, "03 / What was recorded within cyclist hospitalisations?", 24, "bold")
    body += label(24, 70, "CANDIDATE / one-group Sankey | 2021 | widths encode Hospitalisations", 18)
    body += label(24, 150, "Pedal cyclist", 22, "bold") + label(24, 181, "8,163 hospitalisations", 18)
    body += '<rect x="250" y="170" width="18" height="350" fill="#244d68"/>'
    colours = ["#244d68", "#a74527", "#177568", "#77818d"]
    for (name, count), colour in zip(bins, colours):
        h = count * scale
        path = (f'M268,{source_y} C430,{source_y} 430,{target_y} 592,{target_y} '
                f'L592,{target_y+h} C430,{target_y+h} 430,{source_y+h} 268,{source_y+h} Z')
        body += f'<path d="{path}" fill="{colour}" fill-opacity=".55" stroke="{colour}"/>'
        body += f'<rect x="592" y="{target_y}" width="18" height="{h}" fill="{colour}"/>'
        lines = textwrap.wrap(name, 38)
        middle = target_y + h / 2
        for j, line in enumerate(lines):
            body += label(630, middle - 10 + j * 23, line, 18, "bold")
        body += label(630, middle + 18 + (len(lines) - 1) * 23, f"{count:,} / 8,163 = {count/8163:.1%}", 17)
        source_y += h
        target_y += h + 32
    body += label(24, 601, "Links represent classifications, not movement, time order, causation or fault.", 17)
    body += label(24, 628, "Other recorded categories = seven remaining source labels; unspecified remains separate.", 17)
    body += label(24, 655, "Alternative: a row-normalised matrix for comparing groups; narrow screens: bars + table.", 17)
    write("sketch_counterparty.svg", svg("Proposed cyclist counterparty Sankey with count-preserving grouped categories", 1060, 681, body))
    # The matrix retains the full category domain, including the absent cyclist/Train key.
    names = [r["road_user"] for r in groups]
    categories = sorted({r["counterparty"] for r in source})
    values = {(r["road_user"], r["counterparty"]): int(r["hospitalisations"])
              for r in source if r["year"] == "2021"}
    counts = np.array([[values.get((name, category), 0) for category in categories] for name in names])
    shares = counts / counts.sum(axis=1)[:, None] * 100
    assert counts[names.index("Pedal cyclist")].sum() == 8163
    fig, ax = plt.subplots(figsize=(15, 9))
    cmap = LinearSegmentedColormap.from_list("events", ["#f2f6f8", NAVY])
    im = ax.imshow(shares, cmap=cmap, vmin=0, vmax=100, aspect="auto")
    ax.set_yticks(range(len(names)), ["\n".join(textwrap.wrap(n, 25)) for n in names], fontsize=10)
    ax.set_xticks(range(len(categories)), ["\n".join(textwrap.wrap(n, 22)) for n in categories],
                  rotation=35, ha="right", fontsize=10)
    for i in range(len(names)):
        for j in range(len(categories)):
            ax.text(j, i, f"{shares[i,j]:.1f}", ha="center", va="center", fontsize=10,
                    color=cell_text(cmap(shares[i,j] / 100)))
    fig.colorbar(im, ax=ax, orientation="horizontal", pad=.30, fraction=.04,
                 label="Hospitalisations within each road user (%) / 0-100")
    ax.set_title("ALTERNATIVE / Counterparty matrix\n2021 | all 12 road users and all 10 source counterparties | better for between-group comparison", loc="left", pad=18)
    fig.text(.02, .02, "Absent aggregate keys are displayed as zero after reconciliation; unspecified and non-collision stay separate.\nThis alternative shares an encoding with the age heatmap but answers a different question. Count tables remain available.", fontsize=11)
    fig.tight_layout(rect=(0, .07, 1, 1))
    save(fig, "sketch_counterparty_matrix.svg")
    return bins


def preview(bins):
    def figure(name, caption):
        content = (OUT / name).read_text(encoding="utf-8")
        content = content[content.index("<svg"):]
        # Matplotlib SVG IDs repeat between figures; namespace every local reference.
        import re
        prefix = name.replace(".svg", "") + "-"
        ids = re.findall(r'\bid="([^"]+)"', content)
        for old in sorted(ids, key=len, reverse=True):
            content = content.replace(f'id="{old}"', f'id="{prefix}{old}"')
            content = content.replace(f'#{old}"', f'#{prefix}{old}"').replace(f'#{old})', f'#{prefix}{old})')
        # Scoped SVG styles must not override document text styles.
        content = content.replace("<svg ", '<svg class="drawing" ', 1)
        if 'role="img"' not in content.split(">", 1)[0]:
            content = content.replace('<svg class="drawing" ', f'<svg class="drawing" role="img" aria-label="{escape(caption)}" ', 1)
        return f'<figure><div class="drawing-scroll">{content}</div><figcaption>{caption}</figcaption></figure>'
    event_rows = "".join(f"<tr><th scope='row'>{escape(name)}</th><td>{value:,}</td><td>{value/8163:.1%}</td></tr>" for name, value in bins)
    html = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gr_01 / Stand Up 2 design review</title><style>
:root{color-scheme:light;--paper:#f8f7f3;--ink:#142b3d;--muted:#51616a;--line:#d7dcd9;--navy:#244d68;--rust:#a74527}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 Arial,Helvetica,sans-serif}
a{color:var(--navy);text-underline-offset:4px}a:hover{color:var(--rust)}a:focus-visible,summary:focus-visible{outline:3px solid var(--rust);outline-offset:5px}
.skip{position:absolute;left:16px;top:-100px;background:white;padding:12px}.skip:focus{top:8px}header,main,footer{max-width:1200px;margin:auto;padding:32px}
header{border-bottom:1px solid var(--line)}nav{display:flex;gap:12px 25px;flex-wrap:wrap;margin-top:18px}h1,h2,h3{font-family:Georgia,'Times New Roman',serif;line-height:1.15}
h1{font-size:clamp(38px,5.5vw,72px);max-width:900px;margin:22px 0}h2{font-size:clamp(29px,4vw,43px);margin:12px 0 22px}h3{font-size:25px}
p{max-width:80ch}.eyebrow{letter-spacing:.12em;text-transform:uppercase;font-size:13px;font-weight:bold;color:var(--rust)}.status{border-left:4px solid var(--rust);padding:12px 20px;background:white}
section{padding:42px 0;border-bottom:1px solid var(--line);scroll-margin-top:16px}.lead{font-size:21px;max-width:66ch}.stats{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin:24px 0}
.stat{padding:24px;background:white;border-top:3px solid var(--navy)}.stat strong{display:block;font-size:43px}.stat:last-child{border-color:var(--rust)}.stat span{display:block;color:var(--muted)}
figure{min-width:0;margin:25px 0;background:white;border:1px solid var(--line);padding:14px}.drawing-scroll{overflow-x:auto}.drawing{display:block;width:100%;height:auto;min-width:880px}.wireframes{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,1fr);gap:20px}.wireframes .drawing{min-width:0}
figcaption{font-size:15px;color:var(--muted);padding:12px 4px 0}table{border-collapse:collapse;width:100%;font-size:16px}th,td{text-align:left;vertical-align:top;padding:13px 10px;border-bottom:1px solid var(--line)}th{font-weight:600}thead{background:white}caption{text-align:left;font-weight:bold;padding:10px 0}
.table-scroll{overflow-x:auto}code{font-size:.9em;overflow-wrap:anywhere}details{padding:16px 0;border-top:1px solid var(--line)}summary{cursor:pointer;font-weight:bold}.note{color:var(--muted);font-size:15px}.tags{display:flex;gap:10px;flex-wrap:wrap}.tags span{padding:7px 12px;border:1px solid var(--muted);border-radius:4px;font-size:15px}
footer{font-size:15px;color:var(--muted)}@media(max-width:740px){header,main,footer{padding:24px 18px}.stats,.wireframes{grid-template-columns:1fr}.wireframes figure{margin:0}section{padding:32px 0}.stat{padding:18px}th,td{padding:10px 7px}body{font-size:16px}}
@media print{header,main,footer{max-width:none;padding:12px}nav,.skip{display:none}section{break-inside:avoid}.drawing{min-width:0}details{display:block}body{font-size:12px}}
</style></head><body><a class="skip" href="#review">Skip to design review</a>
<header><div class="eyebrow">Gr_01 / COS30045 / Week 11</div><h1>Beyond the Total</h1><p class="lead">Different stories behind Australia's road injuries.</p>
<p class="status"><strong>Stand Up 2 design draft / 22 November 2026.</strong> These are static sketches and proposed interactions. The current D3 website remains at its earlier implementation. Navigation links and disclosure panels on this review page work; chart filters are design specifications.</p>
<nav aria-label="Review sections"><a href="#ready">What to prepare</a><a href="#layout">Wireframes</a><a href="#compare">Compare</a><a href="#events">Events</a><a href="#ages">Ages</a><a href="#handoff">Coding plan</a></nav></header>
<main id="review"><section id="ready"><div class="eyebrow">Review route</div><h2>What this checkpoint gives us</h2>
<p>We use three verified observations to explain our design choices. Open the wireframes, compare each chart with its alternative, then review the interaction and coding specifications. The aim is to justify the design before presenting implementation in Week 12.</p>
<div class="table-scroll"><table><thead><tr><th>Evidence</th><th>Where to review</th><th>Status</th></tr></thead><tbody>
<tr><th scope="row">Data audit and story</th><td><a href="../EDA_AND_STORY.md">EDA findings</a> / <a href="../STORYBOARD.md">storyboard</a></td><td>Documented analysis</td></tr>
<tr><th scope="row">Desktop/mobile layout and chart choices</th><td>Wireframes and sketches below</td><td>Design drafts</td></tr>
<tr><th scope="row">Three Design Book sections</th><td><a href="../design_book/03_design_draft.md">Sections 3.1, 3.2 and 3.3</a></td><td>Written drafts; merge into book later</td></tr>
<tr><th scope="row">Interactions, data and modules</th><td><a href="../CODING_PLAN.md">Coding plan</a></td><td>Specified; new D3 code pending</td></tr>
<tr><th scope="row">Presentation and submission</th><td><a href="../STANDUP_2_REVIEW.md">Review guide and 4:30 talk outline</a></td><td>Five-slide deck, book and portable KNIME prepared; laptop checks pending</td></tr>
</tbody></table></div></section>
<section id="layout"><div class="eyebrow">01 / Website design</div><h2>A guided story, with room to explore</h2>
<p>Read from national change to road-user differences, recorded event categories and age composition. The comparison years stay separate from the profile year. Desktop pairs short explanations with charts; mobile uses selected-group bars and exact tables.</p>
<div class="wireframes">__DESKTOP____MOBILE__</div>
<p class="note">Wireframes show information placement, reading order and narrow-screen alternatives. They are not screenshots of implemented pages. The long mobile drawing is shown large enough to inspect; use its SVG file for slide crops.</p></section>
<section id="compare"><div class="eyebrow">02 / Visualisation design</div><h2>A national decline did not describe every group</h2>
<div class="stats"><div class="stat"><strong>-4.8%</strong>All road users<span>39,866 to 37,966 / 2019-2020</span></div><div class="stat"><strong>+14.1%</strong>Pedal cyclists<span>7,302 to 8,332 / 2019-2020</span></div></div>
<div class="tags" aria-label="Proposed comparison defaults"><span>Year A: 2019 / circle</span><span>Year B: 2020 / diamond</span><span>Selected group: Pedal cyclist</span></div>
__COMPARISON__<details><summary>Why use a dumbbell, and what is its limitation?</summary><p>Two positions on one count axis show direction and magnitude without duplicating bars. Year colour and shape stay fixed when the selected row changes. Grouped bars are more familiar; small differences can be hard to see in either view. We retain exact values and all 12 categories. Cyclists are not the only group to increase: pick-up/van occupants rose from 260 to 300 (+15.4%).</p></details>
<p class="note">The 2019-2020 pair avoids crossing the known 2012 and 2017 recording breaks. It does not establish a cause or a change in exposure-adjusted risk. A brief full-series trend remains in the planned opening.</p></section>
<section id="events"><div class="eyebrow">03 / Recorded event classifications</div><h2>Not every cyclist hospitalisation records another vehicle</h2>
<p><strong>45.4%</strong> of cyclist hospitalisations in 2021 were classified as Non-collision transport accident. The separate unspecified category cannot be reassigned to collision or non-collision.</p>
__COUNTERPARTY__<div class="table-scroll"><table><caption>Sketch grouping / cyclists, 2021 / denominator 8,163</caption><thead><tr><th>Display category</th><th>Hospitalisations</th><th>Within-group share</th></tr></thead><tbody>__EVENT_ROWS__</tbody></table></div>
<details><summary>Grouping and alternative design</summary><p>The compact sketch displays three literal categories and one remainder. The remainder includes Fixed or stationary object, Pedal cycle, Pedestrian or animal, Heavy transport vehicle or bus, 2- or 3- wheeled motor vehicle, Other non-motor vehicle and Train. A zero or absent aggregate contributes no width; all source labels remain in the exact-value table.</p><p>A row-normalised matrix is the alternative if readers need to compare many road users. The one-group Sankey is a candidate for following a total into categories; it still needs usability evaluation. Narrow screens use labelled share bars and a table. No links show a patient journey or fault.</p></details>
__MATRIX__
<p class="note">These 2021 classifications describe the selected year's composition. They do not explain the 2019-2020 increase.</p></section>
<section id="ages"><div class="eyebrow">04 / Age composition</div><h2>Which ages make up each road-user total?</h2>
<p>Cyclists aged 40-64 account for 3,393 of 8,163 hospitalisations in 2021 (<strong>41.6%</strong>). The heatmap puts different group sizes on a common percentage scale, with count as an explicitly labelled alternative mode.</p>
__AGE__<details><summary>How to read the denominator and the colours</summary><p>Each row sums to 100% before rounding. All age groups, including Unknown, contribute to that road user's denominator, with all source sex categories included. The percentage legend stays at 0-100 across years; count mode will use one dataset-wide count domain. Row selection uses an outline, so it does not change colour meaning.</p><p>Bars give a more precise single-group comparison and form the mobile default. Age bands have unequal widths. Composition is not population risk, and Unknown is not excluded to make the profile look cleaner.</p></details></section>
<section id="handoff"><div class="eyebrow">05 / Interaction and implementation handoff</div><h2>What changes when a reader makes a selection?</h2>
<div class="table-scroll"><table><thead><tr><th>Action</th><th>Planned response</th></tr></thead><tbody>
<tr><th scope="row">Change comparison years</th><td>Update dumbbell, national contrast and comparison table only; show a warning when crossing a recording break.</td></tr>
<tr><th scope="row">Choose road user</th><td>Outline its comparison/heatmap row and update the detail-year event view, age bars and detail tables.</td></tr>
<tr><th scope="row">Change detail year</th><td>Update the event and age profiles. Keep comparison years and their heading unchanged.</td></tr>
<tr><th scope="row">Switch count / within-group %</th><td>Update heatmap, mobile age bars, legend, captions and age table together.</td></tr>
<tr><th scope="row">Focus or activate a mark</th><td>Expose exact values and denominators. Native controls and tables offer the same selection path.</td></tr>
<tr><th scope="row">Reset story</th><td>Restore 2019/2020, detail year 2021, Pedal cyclist, percentage mode and no event focus. Keep scroll position.</td></tr>
</tbody></table></div><p>Next implementation order: validate new KNIME outputs, then build the comparison, age profile and counterparty view. Keep the existing D3 data/charts/app split; share constants and selection state. See the <a href="../CODING_PLAN.md">full coding plan</a> for schemas, dependencies and acceptance checks.</p>
<p class="status"><strong>Before Stand Up 2:</strong> export/open the five-slide PPTX, re-import the packaged KNIME workflow, and rehearse with the Markdown notes. Target about 4:30, or about five minutes with a brief existing-web example, following the lecturer's longer format. Submit the three assessment files separately. Participant testing and new production D3 interactions are Week 12 work.</p></section></main>
<footer>Nguyen Huyen Minh Nhat / Le Tuan Huy / Gr_01<br>Source: BITRE September 2023 workbook, Traffic records, sum of Hospitalisations. Static evidence generated from committed analysis CSVs. Rebuild: <code>py tools/build_design_pack.py</code>. AI-assisted drafts require both members' review and explanation in their own words.</footer></body></html>'''
    replacements = {
        "__DESKTOP__": figure("wireframe_desktop.svg", "Desktop / narrative, controls, charts and exact tables."),
        "__MOBILE__": figure("wireframe_mobile.svg", "Mobile / compact selected-group views, labelled controls and exact tables."),
        "__COMPARISON__": figure("sketch_comparison.svg", "Labelled sketch and grouped-bar alternative. Both retain all 12 road-user categories; scroll this review figure on small screens."),
        "__COUNTERPARTY__": figure("sketch_counterparty.svg", "Count-preserving categorical Sankey candidate. Three literal categories plus a documented remainder."),
        "__MATRIX__": figure("sketch_counterparty_matrix.svg", "Labelled alternative: a row-normalised matrix for all 12 road users and all 10 source counterparties."),
        "__AGE__": figure("sketch_age.svg", "All 12 road users and eight age categories. Alternative bars show only cyclists; scroll this review figure on small screens."),
        "__EVENT_ROWS__": event_rows,
    }
    for token, value in replacements.items():
        html = html.replace(token, value)
    write("preview.html", html)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "text.color": INK, "axes.labelcolor": INK, "axes.titlecolor": INK,
                         "xtick.color": INK, "ytick.color": INK,
                         "svg.fonttype": "none", "svg.hashsalt": "gr01-week11-design"})
    wireframes()
    groups = comparison()
    ages(groups)
    preview(counterparty(groups))
    print("Built two wireframes, four chart figures and docs/design/preview.html.")


if __name__ == "__main__":
    main()
