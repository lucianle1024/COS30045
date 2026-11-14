import { buildView, loadData, SEXES } from './data.js';
import { drawTrend, drawRoadUsers, drawDemographics } from './charts.js';

// GenAI prompt summary: coordinate the selected year and road user across
// the three D3 charts, accessible text, controls and the data table.
const number = d3.format(',');
const percent = d3.format('.1%');
const yearSelect = document.querySelector('#year');
const roadSelect = document.querySelector('#road-user');
const reset = document.querySelector('#reset');
const state = { year: 2021, roadUser: 'All road users' };
let data;

document.querySelector('#reload').addEventListener('click', () => location.reload());

function setText(id, value) { document.querySelector(id).textContent = value; }

function render() {
  const view = buildView(data, state.year, state.roadUser);
  yearSelect.value = state.year;
  roadSelect.value = state.roadUser;
  setText('#selection-status', state.roadUser + ' / ' + state.year + ' / ' + number(view.selected) + ' hospitalisations');
  setText('#trend-caption', state.roadUser + ', 2011-2021');
  setText('#trend-insight', 'The selected group recorded ' + number(view.selected) + ' hospitalisations in ' +
    state.year + '. Read the trend alongside the reporting changes marked on the chart.');
  setText('#road-caption', 'Road users in ' + state.year);
  const leader = view.ranking[0];
  setText('#road-insight', leader.road_user + ' had the largest count in ' + state.year + ': ' +
    number(leader.hospitalisations) + ', or ' + percent(leader.hospitalisations / view.national) + ' of the national total.');
  setText('#age-caption', state.roadUser + ' in ' + state.year);
  const largestAge = view.ages.reduce((a, b) => a.total >= b.total ? a : b);
  setText('#age-insight', 'The ' + largestAge.label + ' age group accounted for ' +
    number(largestAge.total) + ' hospitalisations, the largest count for this selection.');
  drawTrend(view, year => { state.year = year; render(); });
  drawRoadUsers(view, roadUser => {
    state.roadUser = state.roadUser === roadUser ? 'All road users' : roadUser;
    render();
  });
  drawDemographics(view);
  setText('#table-caption', state.roadUser + ' in ' + state.year + '. Hospitalisation counts.');
  d3.select('#selected-data tbody').selectAll('tr').data(view.ages, d => d.age).join('tr')
    .selectAll('td').data(d => [d.label, ...SEXES.map(sex => number(d[sex])), number(d.total)])
    .join('td').text(d => d);
  d3.select('#selected-data tfoot').selectAll('tr').data([view]).join('tr')
    .selectAll('td').data(d => ['Total', ...SEXES.map(sex => number(d3.sum(d.ages, row => row[sex]))), number(d.selected)])
    .join('td').text(d => d);
}

try {
  data = await loadData();
  const years = data.annual.map(row => row.year).sort((a, b) => a - b);
  const groups = ['All road users', ...new Set(data.road.map(row => row.road_user).sort())];
  d3.select(yearSelect).selectAll('option').data(years).join('option').attr('value', d => d).text(d => d);
  d3.select(roadSelect).selectAll('option').data(groups).join('option').attr('value', d => d).text(d => d);
  setText('#headline-count', number(data.annual.find(row => row.year === 2021).hospitalisations));
  document.querySelector('#story').hidden = false;
  [yearSelect, roadSelect, reset].forEach(control => { control.disabled = false; });
  yearSelect.addEventListener('change', () => { state.year = Number(yearSelect.value); render(); });
  roadSelect.addEventListener('change', () => { state.roadUser = roadSelect.value; render(); });
  reset.addEventListener('click', () => { state.year = 2021; state.roadUser = 'All road users'; render(); });
  render();
  let frame;
  new ResizeObserver(() => {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(render);
  }).observe(document.querySelector('#trend-chart'));
} catch (error) {
  console.error(error);
  document.querySelector('#story').hidden = true;
  document.querySelector('#load-error').hidden = false;
  setText('#headline-count', 'Unavailable');
  setText('#selection-status', 'The datasets could not be loaded.');
  setText('#error-detail', location.protocol === 'file:' ?
    'Open this page through a local HTTP server so the CSV files can be loaded.' :
    'Check that the three CSV files are present in the data folder, then try again.');
}
