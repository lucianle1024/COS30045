// GenAI prompt summary: load the KNIME exports, validate counts, and derive
// linked views without dropping unknown age or sex categories.
export const AGE_GROUPS = ['0-7', '8-16', '17-25', '26-39', '40-64', '65-74', '75+', 'Missing'];
export const SEXES = ['Male', 'Female', 'Other / not stated'];
const SOURCE_OTHER_SEX = 'intersex or indeterminate or missing';

export function parseRow(row) {
  if (!String(row.year ?? '').trim() || !String(row.hospitalisations ?? '').trim()) {
    throw new Error('A year or count is missing.');
  }
  const year = Number(row.year);
  const hospitalisations = Number(row.hospitalisations);
  if (!Number.isInteger(year) || year < 2011 || year > 2021 ||
      !Number.isInteger(hospitalisations) || hospitalisations < 0) {
    throw new Error('A year or hospitalisation count is invalid.');
  }
  return { ...row, year, hospitalisations };
}

export function validateData(data) {
  const annual = new Map();
  const road = new Map();
  const demographic = new Map();
  const roadAnnual = new Map();
  const seen = new Set();
  for (const row of data.annual) {
    if (annual.has(row.year)) throw new Error('Duplicate annual total.');
    annual.set(row.year, row.hospitalisations);
  }
  for (const row of data.road) {
    const key = JSON.stringify([row.year, row.road_user]);
    if (!row.road_user || road.has(key)) throw new Error('Invalid or duplicate road-user record.');
    road.set(key, row.hospitalisations);
    roadAnnual.set(row.year, (roadAnnual.get(row.year) || 0) + row.hospitalisations);
  }
  for (const row of data.demographic) {
    const key = JSON.stringify([row.year, row.road_user, row.age_group, row.sex]);
    if (seen.has(key) || !AGE_GROUPS.includes(row.age_group) ||
        !['Male', 'Female', SOURCE_OTHER_SEX].includes(row.sex)) {
      throw new Error('Invalid or duplicate demographic record.');
    }
    seen.add(key);
    const roadKey = JSON.stringify([row.year, row.road_user]);
    demographic.set(roadKey, (demographic.get(roadKey) || 0) + row.hospitalisations);
  }
  if (!annual.size || roadAnnual.size !== annual.size || demographic.size !== road.size) {
    throw new Error('The datasets do not cover the same groups and years.');
  }
  for (const [year, count] of annual) {
    if (roadAnnual.get(year) !== count) throw new Error('Road-user totals do not reconcile.');
  }
  for (const [key, count] of road) {
    if (demographic.get(key) !== count) throw new Error('Demographic totals do not reconcile.');
  }
  return data;
}

export async function loadData() {
  const [annual, road, demographic] = await Promise.all([
    d3.csv('data/annual_totals.csv', parseRow),
    d3.csv('data/road_user_by_year.csv', parseRow),
    d3.csv('data/age_sex_by_road_user.csv', parseRow),
  ]);
  return validateData({ annual, road, demographic });
}

export function buildView(data, year, roadUser) {
  const ranking = data.road.filter(row => row.year === year)
    .sort((a, b) => b.hospitalisations - a.hospitalisations || a.road_user.localeCompare(b.road_user));
  const national = data.annual.find(row => row.year === year)?.hospitalisations;
  const trend = (roadUser === 'All road users' ? data.annual :
    data.road.filter(row => row.road_user === roadUser)).slice().sort((a, b) => a.year - b.year);
  const selected = trend.find(row => row.year === year)?.hospitalisations;
  if (national === undefined || selected === undefined) throw new Error('The selected view is unavailable.');
  const ages = AGE_GROUPS.map(age => ({
    age, label: age === 'Missing' ? 'Unknown' : age,
    Male: 0, Female: 0, 'Other / not stated': 0,
  }));
  const byAge = new Map(ages.map(row => [row.age, row]));
  for (const row of data.demographic) {
    if (row.year !== year || (roadUser !== 'All road users' && row.road_user !== roadUser)) continue;
    const sex = row.sex === SOURCE_OTHER_SEX ? 'Other / not stated' : row.sex;
    byAge.get(row.age_group)[sex] += row.hospitalisations;
  }
  for (const row of ages) row.total = SEXES.reduce((sum, sex) => sum + row[sex], 0);
  return { year, roadUser, national, selected, trend, ranking, ages };
}
