import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import vm from 'node:vm';
import { buildView, parseRow, validateData, SEXES } from '../web/data.js';

// AI assistance: test real exported totals, coordinated views and invalid data.
const context = {};
vm.runInNewContext(readFileSync(new URL('../web/vendor/d3.v7.min.js', import.meta.url), 'utf8'), context);
const read = name => Array.from(context.d3.csvParse(
  readFileSync(new URL('../data/processed/' + name, import.meta.url), 'utf8'), parseRow
));
const data = {
  annual: read('annual_totals.csv'),
  road: read('road_user_by_year.csv'),
  demographic: read('age_sex_by_road_user.csv'),
};

test('all actual KNIME exports reconcile', () => {
  assert.equal(validateData(data), data);
  assert.deepEqual([data.annual.length, data.road.length, data.demographic.length], [11, 132, 1683]);
});

test('national totals match the published 2011 and 2021 controls', () => {
  assert.equal(buildView(data, 2011, 'All road users').selected, 34033);
  const view = buildView(data, 2021, 'All road users');
  assert.equal(view.selected, 39505);
  assert.equal(view.ranking[0].road_user, 'Car driver');
  assert.equal(view.ranking[0].hospitalisations, 13327);
});

test('road-user selection updates the entire time series and demographics', () => {
  const view = buildView(data, 2021, 'Pedal cyclist');
  assert.equal(view.selected, 8163);
  assert.equal(view.trend.find(row => row.year === 2011).hospitalisations, 5391);
  assert.equal(view.ages.reduce((sum, row) => sum + row.total, 0), 8163);
});

test('every available year and road-user view retains a matching demographic total', () => {
  for (const row of data.road) {
    const view = buildView(data, row.year, row.road_user);
    assert.equal(view.ages.reduce((sum, age) => sum + age.total, 0), row.hospitalisations);
  }
  const allYears = data.annual.map(row => buildView(data, row.year, 'All road users'));
  assert.equal(allYears.reduce((sum, view) => sum +
    view.ages.reduce((ageSum, age) => ageSum + age['Other / not stated'], 0), 0), 15);
  assert.equal(allYears.reduce((sum, view) => sum + view.ages.find(age => age.age === 'Missing').total, 0), 1);
  assert.equal(SEXES.length, 3);
});

test('blank, fractional and negative counts are rejected; zero is valid', () => {
  for (const hospitalisations of ['', '   ', '-1', '1.5', 'NaN']) {
    assert.throws(() => parseRow({ year: '2021', hospitalisations }));
  }
  assert.equal(parseRow({ year: '2021', hospitalisations: '0' }).hospitalisations, 0);
  assert.throws(() => parseRow({ year: ' ', hospitalisations: '1' }));
  assert.throws(() => parseRow({ year: '2022', hospitalisations: '1' }));
});

test('duplicate records and conflicting totals fail validation', () => {
  assert.throws(() => validateData({ ...data, annual: [...data.annual, data.annual[0]] }));
  assert.throws(() => validateData({ ...data, road: [...data.road, data.road[0]] }));
  const changed = data.demographic.map((row, index) =>
    index === 0 ? { ...row, hospitalisations: row.hospitalisations + 1 } : row
  );
  assert.throws(() => validateData({ ...data, demographic: changed }));
});
