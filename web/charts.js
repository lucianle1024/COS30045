import { SEXES } from './data.js';

// GenAI prompt summary: implement three responsive D3 SVG charts with linked
// selection, keyboard controls, labelled counts, tooltips and reporting breaks.
const colors = { Male: '#244d68', Female: '#177568', 'Other / not stated': '#77818d' };
const number = d3.format(',');
const tooltip = document.querySelector('#chart-tooltip');

function chart(id, label, height) {
  const host = document.querySelector(id);
  const width = Math.max(280, host.clientWidth);
  const svg = d3.select(host).selectAll('svg').data([null]).join('svg')
    .attr('width', width).attr('height', height).attr('viewBox', [0, 0, width, height])
    .attr('role', 'group').attr('aria-label', label);
  svg.selectAll('title').data([label]).join('title').text(d => d);
  return { svg, width, height };
}

function explain(selection, text) {
  function position(event) {
    const bounds = event.currentTarget.getBoundingClientRect();
    const x = event.clientX || bounds.x + bounds.width / 2;
    const y = event.clientY || bounds.y;
    tooltip.style.left = Math.min(Math.max(12, x + 12), window.innerWidth - tooltip.offsetWidth - 12) + 'px';
    tooltip.style.top = Math.min(Math.max(12, y + 14), window.innerHeight - tooltip.offsetHeight - 12) + 'px';
  }
  selection.on('pointerenter.tip focus.tip', function(event, datum) {
    tooltip.textContent = text(datum);
    tooltip.hidden = false;
    position(event);
  }).on('pointermove.tip', position).on('pointerleave.tip blur.tip', () => { tooltip.hidden = true; });
}

function axis(svg, className, transform, axisGenerator) {
  svg.selectAll('g.' + className).data([null]).join('g')
    .attr('class', className + ' axis').attr('transform', transform).call(axisGenerator);
}

export function drawTrend(view, selectYear) {
  const height = 320;
  const { svg, width } = chart('#trend-chart', 'Hospitalisation trend for ' + view.roadUser, height);
  const m = { left: 49, right: 24, top: 44, bottom: 35 };
  const x = d3.scaleLinear().domain(d3.extent(view.trend, d => d.year)).range([m.left, width - m.right]);
  const y = d3.scaleLinear().domain([0, d3.max(view.trend, d => d.hospitalisations) * 1.1]).nice()
    .range([height - m.bottom, m.top]);
  axis(svg, 'grid', 'translate(' + m.left + ',0)', d3.axisLeft(y).ticks(4).tickSize(-(width - m.left - m.right)).tickFormat(''));
  axis(svg, 'x-axis', 'translate(0,' + (height - m.bottom) + ')',
    d3.axisBottom(x).tickValues(view.trend.filter((d, i) => width > 500 || i % 2 === 0).map(d => d.year)).tickFormat(d3.format('d')).tickSizeOuter(0));
  axis(svg, 'y-axis', 'translate(' + m.left + ',0)', d3.axisLeft(y).ticks(4).tickFormat(d3.format('~s')).tickSize(0).tickPadding(8));
  const breaks = [2012, 2017];
  svg.selectAll('line.break').data(breaks).join('line').attr('class', 'break')
    .attr('x1', d => x(d)).attr('x2', d => x(d)).attr('y1', m.top - 15).attr('y2', height - m.bottom)
    .attr('stroke', '#a7afad').attr('stroke-dasharray', '4 4');
  svg.selectAll('text.break-label').data(breaks).join('text').attr('class', 'break-label')
    .attr('x', d => x(d)).attr('y', 17).attr('text-anchor', 'middle').text(d => d + ' break');
  // Separate segments avoid implying continuity across the source's recording breaks.
  const segments = [
    view.trend.filter(d => d.year < 2012),
    view.trend.filter(d => d.year >= 2012 && d.year < 2017),
    view.trend.filter(d => d.year >= 2017),
  ];
  svg.selectAll('path.trend-line').data(segments).join('path').attr('class', 'trend-line')
    .attr('fill', 'none').attr('stroke', '#244d68').attr('stroke-width', 2.5)
    .attr('d', d3.line().x(d => x(d.year)).y(d => y(d.hospitalisations)));
  const points = svg.selectAll('circle.year-point').data(view.trend, d => d.year).join('circle')
    .attr('class', 'year-point').attr('cx', d => x(d.year)).attr('cy', d => y(d.hospitalisations))
    .attr('r', d => d.year === view.year ? 6 : 4).attr('fill', d => d.year === view.year ? '#a74527' : '#244d68')
    .attr('stroke', '#f8f7f3').attr('stroke-width', 2).attr('tabindex', 0).attr('role', 'button')
    .attr('aria-label', d => 'Select ' + d.year + ': ' + number(d.hospitalisations) + ' hospitalisations')
    .attr('aria-pressed', d => d.year === view.year).style('cursor', 'pointer')
    .on('click', (event, d) => selectYear(d.year))
    .on('keydown', (event, d) => {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); selectYear(d.year); }
    });
  explain(points, d => d.year + ' / ' + view.roadUser + ': ' + number(d.hospitalisations));
  svg.selectAll('text.current-value').data(view.trend.filter(d => d.year === view.year)).join('text')
    .attr('class', 'current-value').attr('x', d => x(d.year)).attr('y', d => y(d.hospitalisations) - 15)
    .attr('text-anchor', view.year === 2021 ? 'end' : view.year === 2011 ? 'start' : 'middle')
    .style('fill', '#a74527').style('font-weight', 700).text(d => number(d.hospitalisations));
}

function categoryLines(value, limit) {
  const words = value.split(' ');
  const lines = [''];
  for (const word of words) {
    if (lines[lines.length - 1].length + word.length + 1 > limit && lines.length < 2) lines.push('');
    lines[lines.length - 1] += (lines[lines.length - 1] ? ' ' : '') + word;
  }
  return lines;
}

export function drawRoadUsers(view, selectRoadUser) {
  const height = view.ranking.length * 44 + 64;
  const { svg, width } = chart('#road-chart', 'Road-user hospitalisation counts in ' + view.year, height);
  const m = { left: width < 520 ? 142 : 192, right: 57, top: 18, bottom: 32 };
  const x = d3.scaleLinear().domain([0, d3.max(view.ranking, d => d.hospitalisations)]).nice()
    .range([m.left, width - m.right]);
  axis(svg, 'x-axis', 'translate(0,' + (height - m.bottom) + ')',
    d3.axisBottom(x).ticks(width < 520 ? 3 : 5).tickFormat(d3.format('~s')).tickSizeOuter(0));
  const rows = svg.selectAll('g.rank-row').data(view.ranking, d => d.road_user).join(enter => {
    const group = enter.append('g').attr('class', 'rank-row');
    group.append('rect').attr('class', 'hit-area').attr('fill', 'transparent');
    group.append('rect').attr('class', 'bar');
    group.append('text').attr('class', 'category');
    group.append('text').attr('class', 'value');
    return group;
  }).attr('transform', (d, i) => 'translate(0,' + (m.top + i * 44 + 22) + ')')
    .attr('tabindex', 0).attr('role', 'button').attr('data-road-user', d => d.road_user)
    .attr('aria-label', d => d.road_user + ': ' + number(d.hospitalisations) + ' hospitalisations. Select this group.')
    .attr('aria-pressed', d => d.road_user === view.roadUser)
    .on('click', (event, d) => selectRoadUser(d.road_user))
    .on('keydown', (event, d) => {
      if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); selectRoadUser(d.road_user); }
    });
  rows.select('.hit-area').attr('x', 1).attr('y', -21).attr('width', width - 2).attr('height', 42);
  rows.select('.bar').attr('x', m.left).attr('y', -11).attr('height', 22)
    .attr('width', d => x(d.hospitalisations) - x(0))
    .attr('fill', d => d.road_user === view.roadUser ? '#a74527' : '#244d68');
  rows.select('.category').each(function(d) {
    const lines = categoryLines(d.road_user, width < 520 ? 20 : 26);
    d3.select(this).attr('text-anchor', 'end').selectAll('tspan').data(lines).join('tspan')
      .attr('x', m.left - 12).attr('y', (line, i) => lines.length === 1 ? 4 : -3 + i * 14).text(line => line);
  });
  rows.select('.value').attr('x', d => x(d.hospitalisations) + 7).attr('y', 4)
    .text(d => number(d.hospitalisations));
  explain(rows, d => d.road_user + ' / ' + view.year + ': ' + number(d.hospitalisations));
}

export function drawDemographics(view) {
  const height = view.ages.length * 64 + 50;
  const { svg, width } = chart('#age-chart', 'Age and sex profile: ' + view.roadUser + ' in ' + view.year, height);
  svg.attr('role', 'img');
  const m = { left: 62, right: 50, top: 14, bottom: 30 };
  const bars = view.ages.flatMap((row, index) => SEXES.map((sex, sexIndex) => ({
    age: row.age, label: row.label, sex, count: row[sex], y: m.top + index * 64 + sexIndex * 16,
  })));
  const x = d3.scaleLinear().domain([0, d3.max(bars, d => d.count) || 1]).nice()
    .range([m.left, width - m.right]);
  axis(svg, 'x-axis', 'translate(0,' + (height - m.bottom) + ')',
    d3.axisBottom(x).ticks(width < 520 ? 3 : 5).tickFormat(d3.format('~s')).tickSizeOuter(0));
  svg.selectAll('text.age-label').data(view.ages, d => d.age).join('text').attr('class', 'age-label')
    .attr('x', m.left - 10).attr('y', (d, i) => m.top + i * 64 + 24)
    .attr('text-anchor', 'end').text(d => d.label);
  const rectangles = svg.selectAll('rect.age-bar').data(bars, d => d.age + d.sex).join('rect')
    .attr('class', 'age-bar').attr('x', m.left).attr('y', d => d.y)
    .attr('height', 12).attr('width', d => x(d.count) - x(0)).attr('fill', d => colors[d.sex]);
  rectangles.selectAll('title').data(d => [d]).join('title')
    .text(d => d.label + ', ' + d.sex + ': ' + number(d.count));
  svg.selectAll('text.age-value').data(bars, d => d.age + d.sex).join('text').attr('class', 'age-value')
    .attr('x', d => x(d.count) + 5).attr('y', d => d.y + 10)
    .text(d => d.count ? number(d.count) : '');
  explain(rectangles, d => d.label + ' / ' + d.sex + ': ' + number(d.count));
}
