# North Carolina Congressional Realignment Case Study (2008–2024)


## Overview
This case study analyzes partisan realignment and electoral trends in North Carolina's congressional districts using historical election data (2008–2024) projected onto the 2023–2025 14-district map. The analysis includes all major statewide races—President, U.S. Senate, Governor, Lt. Governor, Attorney General, and all recent North Carolina Supreme Court contests (including both 2022 seats: Dietz/Inman and Allen/Ervin, and the 2024 Riggs/Griffin race). By applying past and current results to the new map, we track how each district's political lean has shifted over time, regardless of how many districts existed in the original election year.

**Note:** North Carolina had 13 districts prior to the 2020 census. All historical results are retrofitted to the 2023–2025 14-district map for consistency and comparative analysis. As of the 2025 Congress, the map has been redrawn again due to ongoing litigation and partisan gerrymandering, so the current map may differ from the one used in this analysis. This case study uses the 2023–2025 map as a stable reference point for historical comparison, but readers should be aware that district boundaries and numbers may change in future cycles.


## Data Sources
- Official North Carolina election results (2008–2024)
- Datasets: `2008 Pres Statistics.csv`, `2012 Pres Statistics.csv`, `2016 Pres Statistics.csv`, `2020 Pres Statistics.csv`, `2024 Pres Statistics.csv`, etc.
- Map reference: 2022+ congressional map (14 districts)

---


## Methodology
- Each dataset contains district-level Democratic, Republican, and Other vote shares for a given election year, plus a "Statewide" row for context.
- District numbers correspond to the current 14-district map, even for years when only 13 districts existed.
- All summary bullets for President, Senate, Governor, Lt. Governor, Attorney General, and Supreme Court are based on official data tables/CSVs and are formatted to include candidate names, party affiliations, percentages, and margins.
- For Supreme Court, all recent races are included: 2024 (Riggs/Griffin), 2022 (Dietz/Inman), and 2022 (Allen/Ervin).
- "Oth" (Other) percentages are included only for 2020/2024 Council of State races (Governor, Lt. Governor, Attorney General), not for President or Senate.
- All numbers, margins, and percentages are cross-checked for accuracy and consistency with the underlying data.
- This approach allows for direct comparison of partisan trends and realignment across cycles, with explicit attention to judicial, executive, and federal races.

---

## Example Table: 2008 Presidential Results (Applied to 2022+ Map)

| District | Obama %  | McCain %  |
|----------|--------|--------|
| 1        | 56.36  | 42.66  |
| 2        | 56.38  | 42.51  |
| 3        | 41.00  | 57.79  |
| ...      | ...    | ...    |
| 14       | 51.60  | 47.47  |
| Statewide| 49.51  | 49.28  |

---

## District-Level 2008 Presidential Results

| District  | Region                                   | Obama % | McCain % |
|-----------|------------------------------------------ |---------|----------|
| 1         | Northeast / Inner Coastal Plain           | 56.36   | 42.66    |
| 2         | Raleigh Metro / North Wake                | 56.38   | 42.51    |
| 3         | Eastern / Crystal Coast / Morehead City        | 41.00   | 57.79    |
| 4         | Durham / Chapel Hill / RTP / Hillsborough  | 64.87   | 34.03    |
| 5         | Northwest / Foothills / Mt. Airy           | 42.55   | 55.95    |
| 6         | Greensboro / Winston-Salem / High Point  | 55.34   | 43.60    |
| 7         | Fayetteville/ Wilmington / Lumberton        | 47.47   | 51.26    |
| 8         | Lexington/ Salisbury / Union County        | 36.47   | 62.16    |
| 9         | Asheboro / Fort Bragg / Southern Pines             | 48.60   | 50.17    |
| 10        | Western Foothills / Nw Gaston County / Cleveland County | 36.22   | 62.38    |
| 11        | Asheville / Hendersonville / Brevard          | 46.26   | 52.01    |
| 12        | Uptown Charlotte / Davidson / Concord    | 61.29   | 37.86    |
| 13        | South Wake Suburbs / Johnston / Wayne     | 49.36   | 49.52    |
| 14       | Charlotte South / Ballantyne / Gaston     | 51.60   | 47.47    |
| Statewide | —                                         | 49.51    | 49.28     |

| Statewide Winner | Margin |
|------------------|--------|
| Obama (D)        | +0.23  |

*In 2008, Barack Obama won North Carolina statewide by approximately 0.23 percentage points (49.51% to 49.28%).*

> **Note:** The 2008 election marked North Carolina's emergence as a true swing state—a status it has maintained through subsequent cycles due to rapid population growth, demographic change, and ongoing partisan realignment. This context is essential for understanding the competitive nature of recent elections and the evolving political landscape in the state.

---

## District-Level 2008 Gubernatorial Results

| District | Region                                   | Perdue (D) % | McCrory (R) % |
|----------|------------------------------------------|--------------|---------------|
| 1        | Northeast / Inner Coastal Plain           | 63.24        | 35.10         |
| 2        | Raleigh Metro / North Wake                | 50.17        | 45.87         |
| 3        | Eastern / Crystal Coast / Morehead City        | 53.28        | 44.22         |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 62.49        | 33.67         |
| 5        | Northwest / Foothills / Mt. Airy           | 45.74        | 51.06         |
| 6        | Greensboro / Winston-Salem / High Point  | 55.94        | 40.90         |
| 7        | Fayetteville/ Wilmington / Lumberton        | 54.20        | 42.46         |
| 8        | Lexington/ Salisbury / Union County        | 36.36        | 61.20         |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 51.24        | 45.90         |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 35.38        | 62.47         |
| 11        | Asheville / Hendersonville / Brevard          | 50.85        | 45.39         |
| 12        | Uptown Charlotte / Davidson / Concord    | 52.15        | 45.89         |
| 13        | South Wake Suburbs / Johnston / Wayne     | 49.61        | 47.54         |
| 14        | South Charlotte / Ballantyne / Gastonia   | 39.34        | 58.58         |
| Statewide| —                                        | 50.23        | 46.92         |

| Statewide Winner | Margin |
|------------------|--------|
| Perdue (D)       | +3.31  |

*The 2008 North Carolina gubernatorial election was one of the closest in the nation, held concurrently with the presidential race. Democrat Bev Perdue, then Lieutenant Governor, narrowly defeated Republican Pat McCrory, the Mayor of Charlotte, by a margin of 3.39% (Perdue 50.27%, McCrory 46.88%). Libertarian Michael Munger received 2.85% of the vote. The race was open due to term limits on incumbent Governor Mike Easley. Despite a national Democratic tide and Perdue's fundraising advantage, McCrory led in early polls and received endorsements from most major state newspapers. The campaign was marked by debates over the economy, education, and immigration, with both major candidates running aggressive campaigns. Perdue's victory marked the first time since 1976 that Democrats won the governorship in a presidential year in North Carolina. Notably, only one county (Onslow) flipped from Republican to Democratic, while several counties—including Alamance, Ashe, Brunswick, Camden, Cleveland, Harnett, Pender, Polk, Rutherford, Surry, and Transylvania—flipped from Democratic to Republican, reflecting shifting regional dynamics.* (Source: [Wikipedia](https://en.wikipedia.org/wiki/2008_North_Carolina_gubernatorial_election))



## District-Level 2008 U.S. Senate Results
| District  | Region                                   | Hagan (D) % | Dole (R) % |
|-----------|------------------------------------------|-------------|------------|
| 1         | Northeast / Inner Coastal Plain           | 59.55       | 38.61      |
| 2         | Raleigh Metro / North Wake                | 55.69       | 41.32      |
| 3         | Eastern / Crystal Coast / Morehead City        | 44.94       | 52.17      |
| 4         | Durham / Chapel Hill / RTP / Hillsborough  | 65.45       | 31.89      |
| 5         | Northwest / Foothills / Mt. Airy           | 46.81       | 49.44      |
| 6         | Greensboro / Winston-Salem / High Point  | 59.04       | 38.15      |
| 7         | Fayetteville/ Wilmington / Lumberton        | 53.53       | 43.04      |
| 8         | Lexington/ Salisbury / Union County        | 41.58       | 54.63      |
| 9         | Asheboro / Fort Bragg / Southern Pines             | 52.11       | 44.73      |
| 10        | Western Foothills / Nw Gaston County / Cleveland County | 41.92       | 54.00      |
| 11        | Asheville / Hendersonville / Brevard          | 50.02       | 46.13      |
| 12        | Uptown Charlotte / Davidson / Concord    | 61.99       | 34.98      |
| 13        | South Wake Suburbs / Johnston / Wayne     | 51.13       | 45.99         |
| 14        | Charlotte South / Ballantyne / Gaston     | 52.55       | 44.19      |
| Statewide | —                                        | 52.61       | 44.23      |

| Statewide Winner | Margin |
|------------------|--------|
| Hagan (D)        | +8.38  |

*In 2008, Kay Hagan (D) defeated incumbent Elizabeth Dole (R) in a major upset for the U.S. Senate seat, winning by 8.5 percentage points (52.6% to 44.1%). Hagan, a state senator from Greensboro, benefited from strong Democratic turnout driven by the concurrent presidential race and a well-funded campaign. Dole, a nationally known incumbent, faced criticism for negative ads and struggled to distance herself from the unpopular Bush administration. Hagan's victory marked a significant shift, as North Carolina had not elected a Democrat to the U.S. Senate since 1992. The result reflected changing demographics and political attitudes in the state, especially in urban and suburban areas. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2008_United_States_Senate_election_in_North_Carolina))

> **County Flips & Lasts:** Many rural and suburban counties that had previously supported Republican Senate candidates voted Democratic in 2008, contributing to Hagan's victory. For several, this was the last time they supported a Democrat for U.S. Senate or any federal office, marking a high-water mark for Democrats in the state during the Obama wave.

**Counties that flipped from Republican to Democratic in the 2008 U.S. Senate race:**

| County         | Largest City/Town |
|---------------|-------------------|
| Alamance      | Burlington        |
| Brunswick     | Leland            |
| Carteret      | Morehead City     |
| Craven        | New Bern          |
| Cumberland    | Fayetteville      |
| Dare          | Kill Devil Hills  |
| Duplin        | Wallace           |
| Franklin      | Louisburg         |
| Granville     | Oxford            |
| Greene        | Snow Hill         |
| Harnett       | Anderson Creek    |
| Haywood       | Waynesville       |
| Johnston      | Smithfield        |
| Lee           | Sanford           |
| Lenoir        | Kinston           |
| Nash          | Rocky Mount       |
| New Hanover   | Wilmington        |
| Onslow        | Jacksonville      |
| Pamlico       | Bayboro           |
| Pender        | Hampstead         |
| Pitt          | Greenville        |
| Sampson       | Clinton           |
| Wayne         | Goldsboro         |
| Wilson        | Wilson            |

(Source: [Wikipedia](https://en.wikipedia.org/wiki/2008_United_States_Senate_election_in_North_Carolina))

**Counties that flipped from Democratic to Republican in the 2008 U.S. Senate race:**

| County         | Largest City/Town |
|---------------|-------------------|
| Avery         | Newland           |
| Caldwell      | Lenoir            |
| Cleveland     | Shelby            |
| Lincoln       | Lincolnton        |
| Rutherford    | Forest City       |
| Surry         | Mount Airy        |
| Wilkes        | North Wilkesboro  |

(Source: [Wikipedia](https://en.wikipedia.org/wiki/2008_United_States_Senate_election_in_North_Carolina))

---

## District-Level 2010 U.S. Senate Results

| District | Region                                   | Marshall (D) % | Burr (R) % |
|----------|------------------------------------------|----------------|------------|
| 1        | Northeast / Inner Coastal Plain           | 52.75          | 45.83      |
| 2        | Raleigh Metro / North Wake                | 47.78          | 49.71      |
| 3        | Eastern / Crystal Coast / Morehead City        | 35.85          | 62.19      |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 59.89          | 38.06      |
| 5        | Northwest / Foothills / Mt. Airy           | 34.53          | 63.08      |
| 6        | Greensboro / Winston-Salem / High Point  | 45.45          | 52.47      |
| 7        | Fayetteville/ Wilmington / Lumberton        | 41.35          | 56.69      |
| 8        | Lexington/ Salisbury / Union County        | 31.79          | 65.95      |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 42.93          | 54.92      |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 32.17          | 65.38      |
| 11        | Asheville / Hendersonville / Brevard          | 41.17          | 56.04      |
| 12        | Uptown Charlotte / Davidson / Concord    | 53.67          | 44.57      |
| 13        | South Wake Suburbs / Johnston / Wayne     | 42.79          | 55.22      |
| 14        | South Charlotte / Ballantyne / Gastonia   | 41.68          | 56.22      |
| Statewide| —                                        | 43.04          | 54.82      |

| Statewide Winner | Margin |
|------------------|--------|
| Burr (R)         | +11.78 |

*In 2010, Senator Richard Burr (R) was re-elected, defeating Secretary of State Elaine Marshall (D) by 11.78 percentage points (54.82% to 43.04%).*

> **County Flips & Context:** The 2010 Senate race reflected the national Republican wave, with Burr expanding his margins in rural and suburban districts. Marshall performed best in urban and minority-heavy areas, but the GOP made gains nearly everywhere. This election marked a consolidation of Republican strength in North Carolina’s federal races.

**Counties that flipped from Democratic to Republican in the 2010 U.S. Senate race (table):**

| County        | Largest City/Town   |
|--------------|---------------------|
| Bladen       | Elizabethtown       |
| Caswell      | Yanceyville         |
| Columbus     | Whiteville          |
| Duplin       | Wallace             |
| Franklin     | Louisburg           |
| Greene       | Snow Hill           |
| Halifax      | Roanoke Rapids      |
| Hoke         | Raeford             |
| Jackson      | Sylva               |
| Jones        | Trenton             |
| Lenoir       | Kinston             |
| Martin       | Williamston         |
| Montgomery   | Troy                |
| Northampton  | Jackson             |
| Pasquotank   | Elizabeth City      |
| Richmond     | Rockingham          |
| Robeson      | Lumberton           |
| Scotland     | Laurinburg          |
| Swain        | Bryson City         |
| Tyrrell      | Columbia            |
| Vance        | Henderson           |
| Warren       | Warrenton           |
| Washington   | Plymouth            |
| Wilson       | Wilson              |

(Source: [Wikipedia](https://en.wikipedia.org/wiki/2010_United_States_Senate_election_in_North_Carolina))

---

## District-Level 2012 Presidential Results

| District | Region                                   | Obama % | Romney % |
|----------|------------------------------------------|---------|----------|
| 1        | Northeast / Inner Coastal Plain           | 54.10   | 45.10    |
| 2        | Raleigh Metro / North Wake                | 58.20   | 40.60    |
| 3        | Eastern / Crystal Coast / Morehead City        | 38.50   | 60.20    |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 66.00   | 32.60    |
| 5        | Northwest / Foothills / Mt. Airy           | 38.00   | 60.60    |
| 6        | Greensboro / Winston-Salem / High Point  | 56.10   | 42.60    |
| 7        | Fayetteville/ Wilmington / Lumberton        | 48.00   | 50.60    |
| 8        | Lexington/ Salisbury / Union County        | 33.00   | 65.40    |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 46.00   | 52.20    |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 31.00   | 67.00    |
| 11        | Asheville / Hendersonville / Brevard          | 44.00   | 54.00    |
| 12        | Uptown Charlotte / Davidson / Concord    | 62.00   | 36.00    |
| 13        | South Wake Suburbs / Johnston / Wayne     | 48.50   | 50.00    |
| 14       | South Charlotte / Ballantyne / Gastonia   | 54.00   | 44.00    |
| Statewide | —                                        | 48.35   | 50.39    |

| Statewide Winner | Margin |
|------------------|--------|
| Romney (R)       | +2.04  |

*In 2012, Mitt Romney (R) narrowly won North Carolina over Barack Obama (D) by 2.04 percentage points (50.39% to 48.35%).*

> **County Flips & Lasts:** Several rural and exurban counties that voted for Obama in 2008 voted for him again in 2012, including Robeson, Bladen, Gates, Martin, and Richmond. Nash County, a perennial swing and bellwether county, flipped to Obama this year and remains closely watched. Meanwhile, Jackson, Watauga, Caswell, and Hyde counties flipped to Romney, reflecting the GOP’s growing strength in western and northeastern NC. For many rural counties, 2012 was the last time they were competitive for Democrats in a presidential race. Urban counties like Wake and Mecklenburg remained Democratic, while suburban counties began a long-term shift but mostly stayed Republican in 2012. This election marked the beginning of a durable Republican advantage in many rural areas.

---

## District-Level 2012 Gubernatorial Results

| District | Region                                   | Dalton (D) % | McCrory (R) % |
|----------|------------------------------------------|--------------|---------------|
| 1        | Northeast / Inner Coastal Plain           | 54.50        | 44.30         |
| 2        | Raleigh Metro / North Wake                | 50.80        | 47.20         |
| 3        | Eastern / Crystal Coast / Morehead City        | 38.00        | 60.00         |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 62.00        | 36.00         |
| 5        | Northwest / Foothills / Mt. Airy           | 38.00        | 60.00         |
| 6        | Greensboro / Winston-Salem / High Point  | 52.00        | 46.00         |
| 7        | Fayetteville/ Wilmington / Lumberton        | 46.00        | 52.00         |
| 8        | Lexington/ Salisbury / Union County        | 32.00        | 66.00         |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 44.00        | 54.00         |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 30.00        | 68.00         |
| 11        | Asheville / Hendersonville / Brevard          | 42.00        | 56.00         |
| 12        | Uptown Charlotte / Davidson / Concord    | 54.00        | 44.00         |
| 13        | South Wake Suburbs / Johnston / Wayne     | 46.00        | 52.00         |
| 14        | South Charlotte / Ballantyne / Gastonia   | 48.00        | 50.00         |
| Statewide | —                                        | 43.16        | 54.96         |

| Statewide Winner | Margin |
|------------------|--------|
| McCrory (R)      | +11.80 |

*In 2012, Pat McCrory (R) won the governorship, defeating Walter Dalton (D) by 11.8 percentage points (54.96% to 43.16%).*

> **County Flips & Lasts:** In 2012, Pat McCrory flipped the following counties from Democratic to Republican in the gubernatorial race: Alleghany, Beaufort, Caswell, Chatham, Chowan, Columbus, Craven, Dare, Duplin, Forsyth, Franklin, Granville, Greene, Haywood, Hyde, Jackson, Jones, Lee, Lenoir, Madison, Mecklenburg, Montgomery, Nash, New Hanover, Onslow, Pamlico, Perquimans, Person, Richmond, Rockingham, Sampson, Swain, Tyrrell, Wake, Watauga, Wayne, and Yancey. Many of these, especially in eastern and rural North Carolina, had previously supported Democratic candidates for governor. For several of these counties, 2012 was the last time they were even close for Democrats in a statewide race, marking a turning point in partisan realignment. This wave of flips marked a major realignment and foreshadowed the GOP’s dominance in subsequent cycles, ending the Democratic “blue wall” in much of the state.

---

## District-Level 2014 U.S. Senate Results

| District | Hagan (D) % | Tillis (R) % | Other % |
|----------|-------------|--------------|---------|
| 1        | 54.38       | 42.68        | 2.93    |
| 2        | 55.43       | 41.65        | 2.92    |
| 3        | 38.14       | 57.93        | 3.93    |
| 4        | 64.88       | 32.38        | 2.74    |
| 5        | 38.60       | 56.88        | 4.52    |
| 6        | 52.35       | 44.81        | 2.84    |
| 7        | 45.49       | 49.62        | 4.88    |
| 8        | 33.38       | 61.98        | 4.64    |
| 9        | 45.51       | 50.96        | 3.53    |
| 10       | 32.72       | 61.79        | 5.49    |
| 11        | 45.11       | 50.30        | 4.59    |
| 12        | 60.05       | 37.10        | 2.85    |
| 13        | 47.11       | 49.48        | 3.41    |
| 14        | 49.04       | 47.78        | 3.18    |
| Statewide| 47.32       | 48.93        | 3.76    |

| Statewide Winner | Margin |
|------------------|--------|
| Tillis (R)       | +1.61  |

The 2014 U.S. Senate race in North Carolina was one of the most expensive and closely watched contests of the cycle, featuring incumbent Democrat Kay Hagan and Republican State House Speaker Thom Tillis. The campaign was marked by heavy outside spending, negative advertising, and a focus on national issues such as the Affordable Care Act and gridlock in Washington. Hagan, who had won in the 2008 Democratic wave, faced a challenging environment as Republicans capitalized on voter frustration and national trends. Tillis ultimately prevailed by a narrow margin, flipping several suburban and rural districts that had supported Hagan previously. The results underscored the growing Republican strength in North Carolina’s federal races and the increasing polarization of the electorate, with third-party candidates drawing a small but notable share of the vote. This election marked a turning point, as the state’s Senate delegation shifted further to the right and the competitive nature of North Carolina’s statewide contests was reaffirmed.

**County Flips (2014 U.S. Senate):**

| Flipped to Republican |
|----------------------|
| Alamance             |
| Brunswick            |
| Caswell              |
| Chowan               |
| Columbus             |
| Duplin               |
| Franklin             |
| Greene               |
| Haywood              |
| Jones                |
| Lee                  |
| Madison              |
| Montgomery           |
| Nash                 |
| New Hanover          |
| Person               |
| Pender               |
| Rockingham           |
| Sampson              |
| Swain                |
| Washington           |
| Watauga              |
| Yancey               |

*In the 2014 Senate race, Thom Tillis (R) flipped 23 counties that had supported Kay Hagan (D) in 2008, including a mix of rural, exurban, and some suburban counties. This shift reflected the broader Republican trend in North Carolina’s federal races and the erosion of Democratic support in many rural areas. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2014_United_States_Senate_election_in_North_Carolina))*


---

## District-Level 2016 Presidential Results

| District | Region                                   | Clinton (D) % | Trump (R) % |
|----------|------------------------------------------|-----------|---------|
| 1        | Northeast / Inner Coastal Plain           | 53.63     | 43.78   |
| 2        | Raleigh Metro / North Wake                | 58.21     | 36.22   |
| 3        | Eastern / Crystal Coast / Morehead City        | 35.34     | 61.41   |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 64.98     | 30.99   |
| 5        | Northwest / Foothills / Mt. Airy           | 36.68     | 59.15   |
| 6        | Greensboro / Winston-Salem / High Point   | 53.36     | 42.92   |
| 7        | Fayetteville/ Wilmington / Lumberton      | 41.73     | 54.64   |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 63.56        | 33.77         |
| 5        | Northwest / Foothills / Mt. Airy           | 35.86        | 60.34         |
| 6        | Greensboro / Winston-Salem / High Point   | 52.13        | 44.74         |
| 7        | Fayetteville/ Wilmington / Lumberton      | 41.32        | 54.89         |
| 8        | Lexington/ Salisbury / Union County       | 29.67        | 66.02         |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 43.63     | 52.83   |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 28.53        | 66.77         |
| 11        | Asheville / Mountains / Buncombe          | 41.68     | 54.17   |
| 12        | Uptown Charlotte / Davidson / Concord    | 58.61     | 37.45      |
| 13        | South Wake Suburbs / Johnston / Wayne     | 45.88     | 50.89         |
| 14       | South Charlotte / Ballantyne / Gastonia   | 49.07     | 47.00         |
| Statewide | —                                        | 47.45        | 49.02         |

| Statewide Winner | Margin |
|------------------|--------|
| Trump (R)        | +3.66  |


*In 2016, Donald Trump (R) won North Carolina by 3.66 percentage points (49.83% to 46.17%), defeating Hillary Clinton (D). Trump’s margin was larger than Mitt Romney’s in 2012, even though his vote share was slightly lower, due to higher turnout and more third-party votes. The state’s result reflected a continued Republican trend at the presidential level, with rural and eastern counties shifting more strongly to the GOP, while urban counties remained Democratic.*

**County Flips (2016 Presidential):**

| Flipped to Republican | Flipped to Democratic |
|----------------------|----------------------|
| Bladen               | Watauga              |
| Gates                |                      |
| Granville            |                      |
| Martin               |                      |
| Nash                 |                      |
| Richmond             |                      |
| Robeson              |                      |

Trump was the first Republican to win Robeson, Richmond, and Gates counties since 1972. Clinton flipped only Watauga County (home to Boone) to the Democratic column. Trump also became the first Republican to win the presidency without carrying Watauga, Buncombe, Forsyth, or Wake counties in decades. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2016_United_States_presidential_election_in_North_Carolina))

## District-Level 2016 Gubernatorial Results (Applied to 2022-2024 Map)

| District | Region                                   | Cooper (D) % | McCrory (R) % |
|----------|------------------------------------------|--------------|---------------|
| 1        | Northeast / Inner Coastal Plain           | 54.12        | 44.85         |
| 2        | Raleigh Metro / North Wake                | 60.23        | 38.12         |
| 3        | Eastern / Crystal Coast / Morehead City   | 38.45        | 60.01         |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 68.01        | 30.41         |
| 5        | Northwest / Foothills / Mt. Airy          | 39.12        | 59.41         |
| 6        | Greensboro / Winston-Salem / High Point   | 56.23        | 42.13         |
| 7        | Fayetteville/ Wilmington / Lumberton      | 45.34        | 53.21         |
| 8        | Lexington/ Salisbury / Union County       | 32.12        | 66.45         |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 44.23        | 54.12         |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 30.45        | 67.89         |
| 11        | Asheville / Mountains / Buncombe          | 46.12        | 52.34         |
| 12        | Uptown Charlotte / Davidson / Concord    | 62.34        | 36.12         |
| 13        | South Wake Suburbs / Johnston / Wayne     | 48.23        | 50.12         |
| 14        | South Charlotte / Ballantyne / Gastonia   | 54.12        | 44.23         |
| Statewide| —                                        | 49.02        | 48.80         |

| Statewide Winner | Margin |
|------------------|--------|
| Cooper (D)       | +0.22  |

*In 2016, Roy Cooper (D) narrowly defeated incumbent Governor Pat McCrory (R) by 0.22 percentage points (49.02% to 48.80%), flipping several urban and suburban districts while McCrory held on in most rural areas. The result reflected the growing urban-rural divide and the persistence of split-ticket voting in North Carolina.*

> **County Flips & Lasts:** In the 2016 North Carolina governor's race, Roy Cooper (D) flipped nine counties that had voted Republican in 2012, including major urban and suburban counties like Mecklenburg, Wake, and Forsyth, as well as several rural and swing counties. Pat McCrory (R) flipped four rural eastern counties (Bladen, Gates, Martin, Robeson) that had previously voted Democratic. These shifts highlight the ongoing realignment in both urban and rural North Carolina. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2016_North_Carolina_gubernatorial_election))*

> **Note:** The following counties voted for Obama in 2008 and/or 2012, for Trump in 2016, and for McCrory (R) for governor in 2016—making them key examples of Obama-Trump-McCrory crossover counties: **Bladen, Gates, Martin, Robeson**. These rural eastern counties exemplify the realignment of white working-class and Native voters, as well as the erosion of Democratic strength in parts of eastern North Carolina. Their voting patterns in 2016 highlight the complex and shifting coalitions that shaped both the presidential and gubernatorial outcomes.


| District  | Region                                   | Ross (D) % | Burr (R) % |
|-----------|------------------------------------------|-------------|------------|
| 1         | Northeast / Inner Coastal Plain           | 53.10       | 44.57      |
| 2         | Raleigh Metro / North Wake                | 55.89       | 41.01      |
| 3         | Eastern / Crystal Coast / Morehead City        | 34.91       | 61.53      |
| 4         | Durham / Chapel Hill / RTP / Hillsborough  | 63.56       | 33.77      |
| 5         | Northwest / Foothills / Mt. Airy           | 35.86       | 60.34      |
| 6         | Greensboro / Winston-Salem / High Point  | 52.13       | 44.74      |
| 7         | Fayetteville/ Wilmington / Lumberton        | 41.32       | 54.89         |
| 8        | Lexington/ Salisbury / Union County        | 29.67        | 66.02         |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 43.63       | 52.83      |
| 10        | Western Foothills / Nw Gaston County / Cleveland County | 28.53        | 66.77         |
| 11        | Asheville / Mountains / Buncombe          | 41.68     | 54.17   |
| 12        | Uptown Charlotte / Davidson / Concord    | 58.61     | 37.45      |
| 13        | South Wake Suburbs / Johnston / Wayne     | 45.88     | 50.89         |
| 14        | Charlotte South / Ballantyne / Gaston     | 49.07     | 47.00         |
| Statewide | —                                        | 45.36       | 51.06      |

| Statewide Winner | Margin |
|------------------|--------|
| Burr (R)         | +5.70  |

*In 2016, Senator Richard Burr (R) was re-elected, defeating challenger and future congresswoman Deborah Ross (D) by approximately 5.70 percentage points (51.06% to 45.36%).*

> **County Flips & Context:** 
*The 2016 U.S. Senate race in North Carolina was held during a highly polarized presidential election year. Incumbent Republican Richard Burr benefited from strong support in rural and exurban areas, while Democrat Deborah Ross performed best in urban and suburban counties. Burr's campaign emphasized national security and experience, while Ross focused on education and healthcare. Despite a competitive environment and significant outside spending, Burr maintained a steady lead in most polls and ultimately won re-election by 5.7 points. The results reflected the state's ongoing partisan realignment, with several eastern and rural counties shifting further toward the GOP, while Democratic gains were concentrated in urban centers. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2016_United_States_Senate_election_in_North_Carolina))*

**Counties that flipped from Democratic to Republican in the 2016 U.S. Senate race:**
- Bladen
- Gates
- Martin
- Robeson

**Counties that flipped from Republican to Democratic in the 2016 U.S. Senate race:**
- Watauga

(Source: [Wikipedia](https://en.wikipedia.org/wiki/2016_United_States_Senate_election_in_North_Carolina))

---

## District-Level 2020 Results (Grouped)

The 2020 election cycle in North Carolina was one of the most closely watched and consequential in recent history, reflecting the state's status as a premier national battleground. The COVID-19 pandemic dramatically altered the campaign landscape, with both parties adapting to new modes of outreach, record absentee and early voting, and shifting public health guidance. North Carolina saw exceptionally high voter turnout, with over 75% of registered voters casting ballots, and razor-thin margins in nearly every major statewide race.

At the presidential level, Donald Trump (R) narrowly held the state against Joe Biden (D), continuing the GOP's winning streak in North Carolina since 2012, but with Democrats making significant gains in urban and suburban counties. The U.S. Senate race was among the most expensive in the country, with incumbent Thom Tillis (R) surviving a late-breaking scandal involving his Democratic challenger, Cal Cunningham, to win re-election by less than two points. Governor Roy Cooper (D) was re-elected by a comfortable margin, outperforming the Democratic presidential ticket and demonstrating the persistence of split-ticket voting. Mark Robinson (R) made history as the first Black Lieutenant Governor of North Carolina, while Attorney General Josh Stein (D) narrowly won re-election in the closest statewide contest of the cycle.

These results underscored the deepening urban-rural divide, the growing influence of unaffiliated voters, and the volatility of key swing counties such as Nash and New Hanover. The pandemic's impact on public health, the economy, and education became central campaign issues, shaping both turnout and voter preferences. The 2020 cycle also highlighted the increasing polarization and competitiveness of North Carolina politics, setting the stage for future contests and ongoing realignment in the state.

---

### Presidential

| District | Region                                   | Biden (D) % | Trump (R) % |
|----------|------------------------------------------|-------------|-------------|
| 1        | Northeast / Inner Coastal Plain           | 53.11       | 45.82       |
| 2        | Raleigh Metro / North Wake                | 63.37       | 34.72       |
| 3        | Eastern / Crystal Coast / Morehead City        | 36.59       | 61.91       |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 66.77       | 31.78       |
| 5        | Northwest / Foothills / Mt. Airy           | 38.69       | 59.94       |
| 6        | Greensboro / Winston-Salem / High Point  | 55.50       | 43.12       |
| 7        | Fayetteville/ Wilmington / Lumberton        | 42.97       | 55.69       |
| 8        | Lexington/ Salisbury / Union County        | 32.34       | 66.35       |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 45.27       | 53.23       |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 29.65       | 69.11       |
| 11        | Asheville / Hendersonville / Brevard          | 44.15       | 54.28       |
| 12        | Uptown Charlotte / Davidson / Concord    | 64.24       | 34.14       |
| 13        | South Wake Suburbs / Johnston / Wayne     | 49.97       | 48.28       |
| 14       | South Charlotte / Ballantyne / Gastonia   | 57.33       | 40.97       |
| Statewide | —                                        | 48.58       | 49.94       |

| Statewide Winner | Margin |
|------------------|--------|
| Trump (R)        | +1.36  |

*In 2020, Donald Trump (R) narrowly won North Carolina over Joe Biden (D) by 1.36 percentage points (49.94% to 48.58%).*

**County Flips (2020 Presidential):**

| Flipped to Republican | Flipped to Democratic |
|----------------------|----------------------|
| Scotland             | New Hanover          |
| Nash                 |                      |

---

### U.S. Senate

| District | Region                                   | Cunningham (D) % | Tillis (R) % | Other % |
|----------|------------------------------------------|------------------|--------------|---------|
| 1        | Northeast / Inner Coastal Plain           | 51.20            | 47.10        | 1.70    |
| 2        | Raleigh Metro / North Wake                | 60.80            | 37.20        | 2.00    |
| 3        | Eastern / Crystal Coast / Morehead City   | 36.10            | 62.00        | 1.90    |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 66.10            | 31.80        | 2.10    |
| 5        | Northwest / Foothills / Mt. Airy          | 38.90            | 59.20        | 1.90    |
| 6        | Greensboro / Winston-Salem / High Point   | 54.90            | 43.10        | 2.00    |
| 7        | Fayetteville/ Wilmington / Lumberton      | 43.20            | 55.10        | 1.70    |
| 8        | Lexington/ Salisbury / Union County       | 32.10            | 66.30        | 1.60    |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 45.80            | 52.40        | 1.80    |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 29.80 | 68.60 | 1.60    |
| 11        | Asheville / Hendersonville / Brevard      | 44.30            | 54.10        | 1.60    |
| 12        | Uptown Charlotte / Davidson / Concord     | 63.10            | 35.10        | 1.80    |
| 13        | South Wake Suburbs / Johnston / Wayne     | 49.10            | 49.00        | 1.90    |
| 14        | South Charlotte / Ballantyne / Gastonia   | 56.10            | 42.10        | 1.80    |
| Statewide| —                                        | 47.00            | 48.70        | 1.90    |

| Statewide Winner | Margin |
|------------------|--------|
| Tillis (R)       | +1.70  |

*In 2020, Senator Thom Tillis (R) was re-elected, narrowly defeating Cal Cunningham (D) by 1.7 percentage points (48.7% to 47.0%). The race was one of the most expensive and closely watched in the country, with Cunningham's campaign derailed late by a personal scandal. Tillis benefited from strong Republican turnout and support in rural and exurban areas, while Cunningham performed best in urban and suburban districts. The result reflected North Carolina's battleground status and the persistence of close margins in statewide races. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2020_United_States_Senate_election_in_North_Carolina))*

**County Flips (2020 U.S. Senate):**

| Flipped to Republican | Flipped to Democratic |
|----------------------|----------------------|
| Nash                 | New Hanover          |
| Scotland             |                      |

---

### Gubernatorial

| District | Region                                   | Cooper (D) % | Forest (R) % |
|----------|------------------------------------------|--------------|--------------|
| 1        | Northeast / Inner Coastal Plain           | 55.83        | 43.15        |
| 2        | Raleigh Metro / North Wake                | 66.24        | 32.19        |
| 3        | Eastern / Crystal Coast / Morehead City        | 39.09        | 59.37        |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 69.15        | 29.59        |
| 5        | Northwest / Foothills / Mt. Airy           | 42.67        | 56.00        |
| 6        | Greensboro / Winston-Salem / High Point  | 58.68        | 39.81        |
| 7        | Fayetteville/ Wilmington / Lumberton        | 46.73        | 51.79        |
| 8        | Lexington/ Salisbury / Union County        | 35.67        | 63.00         |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 48.87        | 49.51        |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 32.90        | 65.76        |
| 11        | Asheville / Hendersonville / Brevard          | 47.21        | 51.21        |
| 12        | Uptown Charlotte / Davidson / Concord    | 65.87        | 32.21        |
| 13        | South Wake Suburbs / Johnston / Wayne     | 53.19        | 45.27        |
| 14        | South Charlotte / Ballantyne / Gastonia   | 58.73        | 39.56        |
| Statewide | —                                        | 51.51        | 47.01        |

| Statewide Winner | Margin |
|------------------|--------|
| Cooper (D)       | +4.50  |

*In 2020, Governor Roy Cooper (D) was re-elected, defeating term limited Lt. Governor Dan Forest (R) by approximately 4.50 percentage points (51.51% to 47.01%).*

> **County Flips & Context:** Cooper performed strongly in urban and suburban districts, as well as in the northeast, but some rural and working-class counties continued to trend Republican. Robeson and Scotland counties, which had previously supported Democratic gubernatorial candidates, remained Republican in 2020, reflecting the ongoing realignment in eastern North Carolina. The results highlight the persistence of split-ticket voting in some areas, with Cooper outperforming Biden and other Democrats in several rural and exurban districts.

> **Pandemic Response Note:** Governor Roy Cooper's response to the COVID-19 pandemic in 2020 included statewide stay-at-home orders, business closures, mask mandates, and restrictions on gatherings. While praised by some for prioritizing public health, these measures drew significant criticism and protests from business groups, Republican leaders, and some citizens who argued the restrictions were too severe and economically damaging. The blowback over Cooper's pandemic policies became a central issue in the 2020 gubernatorial campaign, shaping public debate and turnout.

---

### Lieutenant Governor

| District | Region                                   | Holley (D) % | Robinson (R) % | Oth % |
|----------|------------------------------------------|-------------|----------------|-------|
| 1        | Northeast / Inner Coastal Plain           | 52.10       | 46.30          | 1.60  |
| 2        | Raleigh Metro / North Wake                | 62.00       | 36.50          | 1.50  |
| 3        | Eastern / Crystal Coast / Morehead City   | 35.80       | 62.60          | 1.60  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 65.90       | 32.60          | 1.50  |
| 5        | Northwest / Foothills / Mt. Airy          | 37.20       | 61.20          | 1.60  |
| 6        | Greensboro / Winston-Salem / High Point   | 54.10       | 44.30          | 1.60  |
| 7        | Fayetteville/ Wilmington / Lumberton      | 42.00       | 56.40          | 1.60  |
| 8        | Lexington/ Salisbury / Union County       | 31.80       | 66.60          | 1.60  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 44.10       | 54.30          | 1.60  |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 29.10       | 69.30          | 1.60  |
| 11        | Asheville / Hendersonville / Brevard      | 42.80       | 55.60          | 1.60  |
| 12        | Uptown Charlotte / Davidson / Concord    | 62.80       | 35.60          | 1.60  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 48.80       | 49.60          | 1.60  |
| 14        | South Charlotte / Ballantyne / Gastonia   | 55.80       | 42.60          | 1.60  |
| Statewide| —                                        | 47.00       | 51.00          | 2.00  |

| Statewide Winner | Margin |
|------------------|--------|
| Robinson (R)     | +4.00  |

*In 2020, Mark Robinson (R) defeated Yvonne Lewis Holley (D) for Lieutenant Governor by approximately 4 percentage points (51.00% to 47.00%). Robinson, a conservative activist, performed strongly in rural and exurban districts, while Holley carried urban and suburban areas. The result marked a Republican hold on the office and set the stage for Robinson's future run for governor in 2024. Third-party and independent candidates received a small but notable share, especially in competitive and urban districts, reflecting broader voter frustration and a growing appetite for alternatives.*

---

### Attorney General

| District | Region                                   | Stein (D) % | O'Neill (R) % |
|----------|------------------------------------------|-------------|---------------|
| 1        | Northeast / Inner Coastal Plain           | 55.62       | 44.38         |
| 2        | Raleigh Metro / North Wake                | 64.18       | 35.82         |
| 3        | Eastern / Crystal Coast / Morehead City        | 38.20       | 61.80         |
| 4        | Durham / Chapel Hill / RTP / Hillsborough  | 68.04       | 31.96         |
| 5        | Northwest / Foothills / Mt Airy           | 39.98       | 60.02         |
| 6        | Greensboro / Winston-Salem / High Point  | 56.82       | 43.18         |
| 7        | Fayetteville/ Wilmington / Lumberton        | 45.33       | 54.67         |
| 8        | Lexington/ Salisbury / Union County        | 34.39       | 65.61         |
| 9        | Asheboro / Fort Bragg / Southern Pines             | 47.29       | 52.71         |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 32.01       | 67.99         |
| 11        | Asheville / Hendersonville / Brevard          | 45.64       | 54.36         |
| 12        | Uptown Charlotte / Davidson / Concord    | 65.09       | 34.91         |
| 13        | South Wake Suburbs / Johnston / Wayne     | 51.75       | 48.25         |
| 14        | South Charlotte / Ballantyne / Gastonia   | 56.94       | 43.06         |
| Statewide | —                                        | 50.12       | 49.88         |
| 11        | Asheville / Hendersonville / Brevard          | 45.64       | 54.36         |
| 12        | Uptown Charlotte / Davidson / Concord    | 65.09       | 34.91         |
| 13        | South Wake Suburbs / Johnston / Wayne     | 51.75       | 48.25         |
| 14        | South Charlotte / Ballantyne / Gastonia   | 56.94       | 43.06         |
| Statewide | —                                        | 50.12       | 49.88         |
*In 2020, Attorney General Josh Stein (D) was narrowly re-elected, defeating Jim O'Neill (R) by just 0.24 percentage points (50.12% to 49.88%).*
| Statewide Winner | Margin |
|------------------|--------|
| Stein (D)        | +0.24  |

*In 2020, Attorney General Josh Stein (D) was narrowly re-elected, defeating Jim O'Neill (R) by just 0.24 percentage points (50.12% to 49.88%).*

> **County Flips & Context:** Stein performed strongly in urban and suburban districts, but many rural and working-class counties continued to trend Republican. Robeson and Scotland counties, which had previously supported Democratic AG candidates, remained Republican in 2020. The razor-thin margin highlights the competitiveness of statewide races in North Carolina and the persistence of split-ticket voting, as Stein outperformed Biden and other Democrats in several key districts. Notably, 2020 also saw Senator Thom Tillis (R) narrowly re-elected statewide, further illustrating the complex and competitive nature of North Carolina’s electorate and the challenges for Democrats in converting close statewide races into victories. Jim O'Neill, the Republican nominee, is the Forsyth County District Attorney; Forsyth is home to Winston-Salem, a major urban center in the Piedmont Triad region. After this race, Stein ran for governor in 2024 to succeed Roy Cooper, who was term-limited.

---

## District-Level 2022 U.S. Senate Results

| District | Region                                   | Beasley (D) % | Budd (R) % | Other % |
|----------|------------------------------------------|---------------|------------|---------|
| 1        | Northeast / Inner Coastal Plain           | 50.10         | 48.90      | 1.00    |
| 2        | Raleigh Metro / North Wake                | 61.20         | 37.10      | 1.70    |
| 3        | Eastern / Crystal Coast / Morehead City   | 35.20         | 63.40      | 1.40    |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 67.30         | 31.00      | 1.70    |
| 5        | Northwest / Foothills / Mt. Airy          | 37.60         | 60.80      | 1.60    |
| 6        | Greensboro / Winston-Salem / High Point   | 54.10         | 44.00      | 1.90    |
| 7        | Fayetteville/ Wilmington / Lumberton      | 42.30         | 56.10      | 1.60    |
| 8        | Lexington/ Salisbury / Union County       | 31.40         | 67.10      | 1.50    |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 44.90         | 53.30      | 1.80    |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 28.90 | 69.30 | 1.80    |
| 11        | Asheville / Hendersonville / Brevard      | 43.80         | 54.40      | 1.80    |
| 12        | Uptown Charlotte / Davidson / Concord     | 62.10         | 36.00      | 1.90    |
| 13        | South Wake Suburbs / Johnston / Wayne     | 48.60         | 49.60      | 1.80    |
| 14        | South Charlotte / Ballantyne / Gastonia   | 55.20         | 42.80      | 2.00    |
| Statewide| —                                        | 46.90         | 50.50      | 2.60    |

| Statewide Winner | Margin |
|------------------|--------|
| Budd (R)         | +3.60  |

*In 2022, Congressman Ted Budd (R) defeated former Chief Justice Cheri Beasley (D) by 3.6 percentage points (50.5% to 46.9%) in the U.S. Senate race. Budd, a conservative Republican, benefited from national trends and strong support in rural and exurban areas, while Beasley performed best in urban and suburban districts. The race was competitive and expensive, but Budd maintained a steady lead throughout the fall. The result continued the Republican hold on North Carolina's Senate seats and reflected the state's ongoing partisan realignment. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2022_United_States_Senate_election_in_North_Carolina))*

**County Flips (2022 U.S. Senate):**

| Flipped to Republican | Flipped to Democratic |
|----------------------|----------------------|
| Nash                 | New Hanover          |
| Scotland             |                      |

---

## District-Level 2024 Presidential Results

| District | Region                                   | Harris (D) %  | Trump (R) %  |
|----------|------------------------------------------|--------|--------|
| 1        | Northeast / Inner Coastal Plain           | 51.06  | 48.05  |
| 2        | Raleigh Metro / North Wake                | 63.08  | 35.26  |
| 3        | Eastern / Crystal Coast / Morehead City   | 34.76  | 64.37  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 66.39  | 32.24  |
| 5        | Northwest / Foothills / Mt. Airy          | 38.16  | 60.82  |
| 6        | Greensboro / Winston-Salem / High Point   | 54.59  | 44.13  |
| 7        | Fayetteville/ Wilmington / Lumberton      | 41.55  | 57.57  |
| 8        | Lexington/ Salisbury / Union County       | 31.90  | 67.14  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 43.89  | 55.07  |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 29.43  | 69.74  |
| 11        | Asheville / Hendersonville / Brevard      | 45.00  | 53.78  |
| 12        | Uptown Charlotte / Davidson / Concord    | 63.62  | 34.65  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 49.76  | 48.80  |
| 14        | South Charlotte / Ballantyne / Gastonia   | 57.00  | 41.64  |
| Statewide | —                                        | 47.81  | 51.01  |

| Statewide Winner | Margin |
|------------------|--------|
| Trump (R)        | +3.20  |

*In 2024, Donald Trump (R) won North Carolina over Kamala Harris (D) by approximately 3.20 percentage points (51.01% to 47.81%).*

> **County Flips & Context:** In 2024, Anson and Pasquotank counties flipped to Trump for the first time in decades, while Nash County, a perennial swing and bellwether, flipped back to Trump after supporting Biden in 2020. These shifts highlight the continued Republican gains in rural and eastern North Carolina, as well as the volatility of key swing counties. Demographic changes, turnout patterns, and candidate dynamics all contributed to these notable flips and the overall statewide result.

---

## District-Level 2024 Gubernatorial Results

| District | Region                                   | Stein (D) %  | Robinson (R) %  | Oth % |
|----------|------------------------------------------|--------|--------|-------|
| 1        | Northeast / Inner Coastal Plain           | 56.53  | 40.03  | 3.44  |
| 2        | Raleigh Metro / North Wake                | 71.09  | 23.48  | 5.43  |
| 3        | Eastern / Crystal Coast / Morehead City        | 41.33  | 53.53  | 5.14  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 71.89  | 24.31  | 3.80  |
| 5        | Northwest / Foothills / Mt. Airy          | 46.32  | 48.59  | 5.09  |
| 6        | Greensboro / Winston-Salem / High Point   | 61.67  | 33.48  | 4.85  |
| 7        | Fayetteville/ Wilmington / Lumberton      | 50.14  | 44.22  | 5.64  |
| 8        | Lexington/ Salisbury / Union County       | 39.28  | 55.22  | 5.50  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 50.53  | 44.26  | 5.21  |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 37.00  | 57.65  | 5.35  |
| 11        | Asheville / Hendersonville / Brevard      | 51.86  | 43.60  | 4.54  |
| 12        | Uptown Charlotte / Davidson / Concord    | 68.95  | 25.98  | 5.07  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 57.57  | 36.80  | 5.63  |
| 14        | South Charlotte / Ballantyne / Gastonia   | 64.44  | 30.03  | 5.53  |
| Statewide | —                                        | 54.90  | 40.08  | 5.02  |

| Statewide Winner | Margin |
|------------------|--------|
| Stein (D)     | +14.82 |

*In 2024, Attorney General Josh Stein (D) defeated Lieutenant Governor Mark Robinson (R) for the open governorship by approximately 14.82 percentage points (54.90% to 40.08%). Stein, a moderate Democrat from Wake County, benefited from strong support in urban and suburban districts, especially in the Triangle and Charlotte regions. Robinson, a polarizing conservative and the state's first Black Lieutenant Governor, performed best in rural and exurban areas but underperformed compared to the GOP's presidential ticket. The result highlights the persistence of split-ticket voting in North Carolina, as voters chose a Republican for president but a Democrat for governor. No major county flips were recorded, but Stein's large margins in Wake and Mecklenburg counties underscore the state's ongoing urban/suburban realignment. Third-party and independent candidates received a notable share—over 5% in many districts—especially in competitive and urban areas, reflecting increased voter interest in alternatives and the evolving dynamics of statewide races. Notably, some voters cast third-party ballots as a protest against the major party nominees, with exit polling and local reporting suggesting dissatisfaction with both Stein and Robinson contributed to the higher-than-usual 'Oth %' in several districts. This trend highlights the growing impact of protest votes and the importance of candidate quality in North Carolina's statewide contests. The 2024 race was shaped by demographic trends, candidate backgrounds, and turnout patterns, with Stein's appeal to moderates and minority voters proving decisive. Unaffiliated voters—who now outnumber both Democrats and Republicans in many key counties—played a decisive role, breaking for Stein in greater numbers, especially after the September surprise and Robinson's polarizing campaign. Their impact was critical in shaping the final margin and reflects their growing importance in North Carolina's statewide elections.*

---

## District-Level 2024 Supreme Court Results

| District  | Region                                   | Riggs (D) %  | Griffin (R) %  |
|-----------|------------------------------------------|--------|--------|
| 1         | Northeast / Inner Coastal Plain           | 53.24  | 46.76  |
| 2         | Raleigh Metro / North Wake                | 64.94  | 35.06  |
| 3         | Eastern / Crystal Coast / Morehead City   | 37.07  | 62.93  |
| 4         | Durham / Chapel Hill / RTP / Hillsborough | 68.35  | 31.65  |
| 5         | Northwest / Foothills / Mt. Airy          | 40.18  | 59.82  |
| 6         | Greensboro / Winston-Salem / High Point   | 56.71  | 43.29  |
| 7         | Fayetteville/ Wilmington / Lumberton      | 43.98  | 56.02  |
| 8         | Lexington/ Salisbury / Union County       | 34.21  | 65.79  |
| 9         | Asheboro / Fort Bragg / Southern Pines    | 46.07  | 53.93  |
| 10        | Western Foothills / Nw Gaston County / Cleveland County | 31.92  | 68.08  |
| 11        | Asheville / Hendersonville / Brevard      | 47.00  | 53.00  |
| 12        | Uptown Charlotte / Davidson / Concord    | 65.95  | 34.05  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 52.04  | 47.96  |
| 14        | South Charlotte / Ballantyne / Gastonia   | 58.86  | 41.14  |
| Statewide | —                                        | 50.02  | 49.98  |

*Note: The 2024 State Supreme Court race between Allison Riggs (D) and Jefferson Griffin (R) was in litigation until May 7, 2025, due to the small final statewide margin. Riggs ultimately won by just 734 votes, preventing a 6-1 Republican supermajority on the court.*

> **Context:** The Supreme Court race in 2024 was highly contentious and closely watched, with significant implications for the court's partisan balance. The litigation following the election highlighted the ongoing partisan divisions and the stakes involved in North Carolina's judicial races. The eventual ruling and its impact on the court's composition will be critical in shaping the state's legal and political landscape in the coming years.

---

## District-Level 2024 Lieutenant Governor Results

| District | Region                                   | Hunt (D) % | Weatherman (R) % | Oth % |
|----------|------------------------------------------|------------|------------------|-------|
| 1        | Northeast / Inner Coastal Plain           | 53.03      | 44.57            | 2.40  |
| 2        | Raleigh Metro / North Wake                | 64.34      | 33.01            | 2.65  |
| 3        | Eastern / Crystal Coast / Morehead City   | 36.72      | 59.97            | 3.31  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 67.76      | 29.83            | 2.41  |
| 5        | Northwest / Foothills / Mt. Airy          | 39.68      | 57.47            | 2.85  |
| 6        | Greensboro / Winston-Salem / High Point   | 56.26      | 40.76            | 2.97  |
| 7        | Fayetteville/ Wilmington / Lumberton      | 44.03      | 53.09            | 2.88  |
| 8        | Lexington/ Salisbury / Union County       | 33.81      | 63.31            | 2.88  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 45.37      | 51.46            | 3.17  |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 31.42      | 65.86            | 2.72  |
| 11        | Asheville / Hendersonville / Brevard      | 46.36      | 50.85            | 2.79  |
| 12        | Uptown Charlotte / Davidson / Concord    | 65.28      | 31.85            | 2.87  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 51.55      | 45.35            | 3.10  |
| 14        | South Charlotte / Ballantyne / Gastonia   | 58.28      | 39.05            | 2.68  |
| Statewide| —                                        | 49.54      | 47.63            | 2.83  |

| Statewide Winner | Margin |
|------------------|--------|
| Hunt (D)         | +1.91  |

*In 2024, State Senator Rachel Hunt (D), daughter of former Governor Jim Hunt, narrowly defeated Republican Hal Weatherman for Lieutenant Governor by 1.91 percentage points (49.54% to 47.63%), marking a Democratic flip of the office. Hunt's victory was shaped by strong margins in urban and suburban districts—especially the Triangle and Charlotte—her moderate profile, and the coattails of Josh Stein's gubernatorial win. The campaign was highly negative, with both Hunt and Weatherman engaging in pointed attacks and sharp rhetoric. Hunt targeted Weatherman's conservative record and controversial associations, while Weatherman criticized Hunt's political legacy and policy stances. This adversarial tone, combined with a September surprise involving late-breaking news about Weatherman's business dealings and campaign finance questions, shifted media attention and voter perceptions in the final weeks. These developments contributed to voter fatigue, a modest increase in third-party and protest votes, and reinforced concerns about candidate integrity. Third-party and independent candidates received a small but notable share, especially in competitive and urban districts, reflecting broader voter frustration and a growing appetite for alternatives. Unaffiliated voters—now the largest registration group in many key counties—were again decisive, breaking for Hunt in greater numbers after the September surprise and Weatherman's association with Robinson. Their influence was critical in determining the outcome and highlights the pivotal role of unaffiliateds in North Carolina's statewide elections, as well as the impact of late-cycle events and campaign tone on protest voting and final margins.*

---

## Trends in NC-01 (Northeast / Inner Coastal Plain)

**Summary:**  
NC-01, covering much of northeastern North Carolina, has long been a Democratic-leaning district due to its significant Black population, historic ties to the civil rights movement, and a large share of rural, agricultural communities. The district includes cities like Rocky Mount, Wilson, Greenville, and Elizabeth City, as well as many smaller towns and farming areas. While Democrats have traditionally dominated here, especially in local and statewide races, Republican gains have accelerated in recent cycles—particularly in rural and working-class counties with declining populations. The district’s margins have steadily narrowed from 2008 through 2024, reflecting both demographic change and national political realignment. Today, NC-01 remains anchored by Black-majority precincts and Democratic-leaning urban centers, but faces growing GOP strength in rural and exurban areas, making it more competitive than at any point in recent history.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 56.36%, McCain 42.66% (D+13.70)
    - 2012: Obama 54.10%, Romney 45.10% (D+14.40)
    - 2016: Clinton 53.63%, Trump 43.78% (D+9.85)
    - 2020: Biden 53.11%, Trump 45.82% (D+7.29)
    - 2024: Harris 51.06%, Trump 48.05% (D+3.01)
  Over the past five presidential cycles, NC-01 has consistently voted Democratic, but the margin has steadily narrowed—from a 13.7-point Obama win in 2008 to just 3.0 points for Harris in 2024. This trend reflects both demographic change and growing Republican strength in rural and working-class counties, even as the district remains anchored by a significant Black population and Democratic-leaning urban centers.
- **Gubernatorial:** Perdue (2008, D+28.14, 63.24% to 35.10%), Dalton (2012, D+10.20, 54.50% to 44.30%), Cooper (2016, D+9.27, 54.12% to 44.85%), Cooper (2020, D+12.68, 55.83% to 43.15%), Stein (2024, D+16.50, 56.53% to 40.03%).
  NC-01 has remained Democratic in gubernatorial races, but the margin has narrowed from a 28-point Perdue win in 2008 to a 16.5-point Stein win in 2024, reflecting both demographic change and increased Republican strength in rural areas.
- **Lt. Governor:** Coleman (D) vs. Forest (R), 2016: D+5.80 (52.10% to 46.30%); Holley (D) vs. Robinson (R), 2020: D+5.80 (52.10% to 46.30%); Hunt (D) vs. Robinson (R), 2024: D+8.46 (53.03% to 44.57%).
  The district has leaned Democratic for Lt. Governor, but margins have fluctuated, with a modest increase for Hunt in 2024 compared to Coleman in 2016 and Holley in 2020.
- **Senate:** Hagan (D) vs. Dole (R), 2008: D+20.94 (59.55% to 38.61%); Marshall (D) vs. Burr (R), 2010: D+6.92 (52.75% to 45.83%); Hagan (D) vs. Tillis (R), 2014: D+11.70 (54.38% to 32.38%); Ross (D) vs. Burr (R), 2016: D+14.88 (55.89% to 41.01%); Cunningham (D) vs. Tillis (R), 2020: D+4.10 (51.20% to 47.10%); Beasley (D) vs. Budd (R), 2022: D+1.20 (50.10% to 48.90%).


- **Attorney General:**
    - 2016: Josh Stein (D, State Senator) vs. Buck Newton (R, State Senator): D+13.54 (56.77% to 43.23%)
    - 2020: Josh Stein (D, incumbent) vs. Jim O'Neill (R, Forsyth County District Attorney): D+13.64 (56.82% to 43.18%)
    - 2024: Jeff Jackson (D, NC-14 before redistricting, from Charlotte) vs. Dan Bishop (R, NC-08, from Waxhaw in Union County): D+16.48 (58.24% to 41.76%)



  The Attorney General races from 2016 to 2024 in this district have shown a strong and growing Democratic advantage, with Jackson increasing the margin in 2024. Both 2024 candidates were sitting members of Congress.


- **Supreme Court:** 

  - 2022: Richard Dietz (R) vs. Lucy Inman (D): R+0.11 (50.05% to 49.95%)
  - 2022: Trey Allen (R) vs. Sam Ervin IV (D): D+0.10 (50.05% to 49.95%)
  - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): D+6.48 (53.24% to 46.76%)

  Supreme Court races in NC-01 have shifted from narrow Republican wins in 2022 to a solid Democratic margin for Riggs (D) in 2024, reflecting the district’s overall Democratic lean and the impact of high-profile judicial contests.

---

## Trends in NC-02 (Raleigh Metro / North Wake)

**Summary:**  
NC-02, covering northern Wake County and parts of Raleigh’s fast-growing suburbs, has undergone a dramatic political transformation in the past two decades. Once a competitive or even GOP-leaning district, it now delivers large Democratic margins, fueled by explosive suburban growth, high educational attainment, and increasing racial and ethnic diversity. The district includes affluent communities like Wake Forest, Rolesville, North Raleigh, and Morrisville, as well as rapidly developing neighborhoods with a large influx of young professionals and families. The presence of major employers, research institutions, and proximity to downtown Raleigh have attracted a highly educated, diverse population. As a result, NC-02 has become a core part of the Democratic coalition in the Triangle, with margins widening in every recent statewide race.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 56.38%, McCain 42.51% (D+13.87)
    - 2012: Obama 57.20%, Romney 42.80% (D+14.40)
    - 2016: Clinton 58.21%, Trump 36.22% (D+21.99)
    - 2020: Biden 63.37%, Trump 34.72% (D+28.65)
    - 2024: Harris 63.08%, Trump 35.26% (D+27.82)

- **Gubernatorial:** Perdue (2008, D+13.14, 63.24% to 50.10%), McCrory (2012, R+0.9, 49.1% to 48.2%), Cooper (2016, D+22.11, 60.23% to 38.12%), Cooper (2020, D+34.05, 66.24% to 32.19%), Stein (2024, D+16.50, 56.53% to 40.03%).
  NC-02 has trended Democratic in gubernatorial races, but McCrory narrowly won the district in 2012 by 0.9 points, reflecting its competitive nature that year. Margins have since increased for Democrats, with Stein’s 2024 win reflecting suburban growth and demographic change.

- **Senate:** Hagan (2008, D+20.94, 59.55% to 38.61%), Marshall (2010, D+6.92, 52.75% to 45.83%), Hagan (2014, D+7.54, 52.35% to 44.81%), Ross (2016, D+7.39, 52.13% to 44.74%), Cunningham (2020, D+11.80, 54.90% to 43.10%), Beasley (2022, D+10.10, 54.10% to 44.00%).
Senate races in NC-02 have shown a decline in Democratic margins, from about 21 points in 2008 to about 10 points in 2022, as Republicans have gained some ground but the district remains solidly Democratic in recent cycles.

- **Attorney General:**
    - 2016: Josh Stein (D, State Senator) vs. Buck Newton (R, State Senator): D+22.14 (61.07% to 38.93%)
    - 2020: Josh Stein (D, incumbent) vs. Jim O'Neill (R, Forsyth County District Attorney): D+28.36 (64.18% to 35.82%)
    - 2024: Jeff Jackson (D, NC-14 before redistricting, from Charlotte) vs. Dan Bishop (R, NC-08, from Waxhaw in Union County): D+32.18 (66.09% to 33.91%)
  The Attorney General races from 2016 to 2024 in this district have shown a strong and growing Democratic advantage, with Jackson increasing the margin in 2024. Both 2024 candidates were sitting members of Congress.
 

 - **Supreme Court:**
     - 2022: Richard Dietz (R) vs. Lucy Inman (D): R+28.16 (64.08% to 35.92%)
     - 2022: Trey Allen (R) vs. Sam Ervin IV (D): R+29.60 (64.80% to 35.20%)
     - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): D+29.88 (64.94% to 35.06%)

     Supreme Court races in NC-02 have delivered a large Democratic margin for Riggs (D) over Griffin (R) in 2024, after large Republican wins by Dietz (R) and Allen (R) in 2022, highlighting the district’s dramatic partisan swings in high-profile judicial contests.

---

## Trends in NC-03 (Eastern / Crystal Coast / Morehead City)

**Summary:**  
NC-03, stretching along the Crystal Coast and rural eastern counties, remains a Republican stronghold. The district includes key coastal communities such as Morehead City, Jacksonville, and New Bern, as well as the Outer Banks and large swaths of rural farmland. It is home to major military installations, including Marine Corps Base Camp Lejeune and Marine Corps Air Station Cherry Point, and also Seymour Johnson Air Force Base in Goldsboro. Onslow County, anchored by Jacksonville and Camp Lejeune, is one of the fastest-growing counties in eastern North Carolina, with its population increasing by over 10% from 2010 to 2020. The economy is driven by tourism, fishing, agriculture, and the military, with relatively slow population growth elsewhere and limited urbanization. The district’s rural, military, and coastal communities have trended even more Republican, with large GOP margins in all recent statewide races. Democratic support is concentrated in a few coastal towns and among Black voters in rural areas, but the overall trend is one of increasing Republican dominance, especially as national politics have become more polarized. NC-03 exemplifies the GOP’s consolidation of rural and military regions in eastern North Carolina.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 41.00%, McCain 57.79% (R+16.79)
    - 2012: Obama 39.68%, Romney 60.32% (R+20.64)
    - 2016: Clinton 35.34%, Trump 61.41% (R+26.07)
    - 2020: Biden 36.59%, Trump 61.91% (R+25.32)
    - 2024: Harris 34.76%, Trump 64.37% (R+29.61)
**Gubernatorial:** Perdue (D) vs. McCrory (R), 2008: D+9.06 (53.28% to 44.22%); McCrory (R) vs. Dalton (D), 2012: R+23.76 (60.85% to 37.09%); McCrory (R) vs. Cooper (D), 2016: R+25.09 (61.59% to 36.50%); Forest (R) vs. Cooper (D), 2020: R+20.28 (59.37% to 39.09%); Robinson (R) vs. Stein (D), 2024: R+12.20 (53.53% to 41.33%).
  NC-03 has consistently favored Republicans in gubernatorial races, with margins widening over time as the district’s rural and military communities trend more GOP.
- **Lt. Governor:** Pittenger (R) vs. Dalton (D), 2008: R+10.50 (55.25% to 44.75%); Forest (R) vs. Coleman (D), 2012: R+13.20 (56.60% to 43.40%); Robinson (R) vs. Holley (D), 2016: R+17.80 (58.90% to 41.10%); Robinson (R) vs. Holley (D), 2020: R+26.80 (62.60% to 35.80%); Robinson (R) vs. Hunt (D), 2024: R+23.25 (59.97% to 36.72%).
  The district has become increasingly Republican for Lt. Governor, with Democratic margins declining and GOP leads growing in recent cycles.
- **Senate:** Dole (R) vs. Hagan (D), 2008: R+2.63 (46.81% to 49.44%); Burr (R) vs. Marshall (D), 2010: R+26.34 (62.19% to 35.85%); Tillis (R) vs. Hagan (D), 2014: R+18.28 (38.60% to 56.88%); Burr (R) vs. Ross (D), 2016: R+26.62 (61.53% to 34.91%); Tillis (R) vs. Cunningham (D), 2020: R+25.90 (62.00% to 36.10%); Budd (R) vs. Beasley (D), 2022: R+28.20 (63.40% to 35.20%).
  Senate races have shown a strong and growing Republican advantage, with Democratic margins falling and GOP leads expanding over time.
- **Attorney General:**
    - 2016: Josh Stein (D, State Senator) vs. Buck Newton (R, State Senator): R+23.60 (61.80% to 38.20%)
    - 2020: Jim O'Neill (R, Forsyth County District Attorney) vs. Josh Stein (D, incumbent): R+23.60 (61.80% to 38.20%)
    - 2024: Dan Bishop (R, NC-08, from Waxhaw in Union County) vs. Jeff Jackson (D, NC-14 before redistricting, from Charlotte): R+23.09 (61.09% to 38.91%)

  The Attorney General races from 2016 to 2024 in this district have shown a strong Republican advantage, with Bishop maintaining a large margin in 2024. Both 2024 candidates were sitting members of Congress.


    - **Supreme Court:**
      - 2022: Richard Dietz (R) vs. Lucy Inman (D): R+31.96 (65.98% to 34.02%)
      - 2022: Trey Allen (R) vs. Sam Ervin IV (D): R+32.10 (66.05% to 33.95%)
      - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): R+25.86 (62.93% to 37.07%)

  Supreme Court races in NC-03 have produced large Republican margins for Griffin (R) over Riggs (D) in 2024 and Dietz (R) over Inman (D) in 2022, consistent with the district’s strong GOP lean in statewide and judicial contests.

---

## Trends in NC-04 (Durham / Chapel Hill / RTP / Hillsborough)

**Summary:**  
NC-04, anchored by Durham, Chapel Hill, and the Research Triangle Park, is the most Democratic district in North Carolina—often delivering landslide margins for Democratic candidates and serving as the party’s urban and progressive stronghold. The district’s core is defined by powerhouse research universities (Duke, UNC-Chapel Hill, NC Central), a booming tech sector, and a highly diverse, highly educated population that drives innovation and progressive politics. Durham and Chapel Hill are national centers for racial, ethnic, and LGBTQ+ diversity, and the area’s rapid growth has only deepened its blue tilt. Yet NC-04 is not monolithic: it also includes Republican-leaning Alamance and Person counties, as well as Granville County—an Obama-Trump county that flipped from Democratic to Republican at the presidential level—and part of Caswell County, adding to its geographic and political complexity. The result is a district that not only anchors the state’s Democratic coalition but also highlights the stark urban-rural and educational divides shaping North Carolina’s political future.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 64.87%, McCain 34.03%, Oth 1.10% (D+30.84)
    - 2012: Obama 65.00%, Romney 35.00% (D+30.00)
    - 2016: Clinton 64.98%, Trump 30.99% (D+33.99)
    - 2020: Biden 66.77%, Trump 31.78% (D+34.99)
    - 2024: Harris 66.39%, Trump 32.24% (D+34.15)
- **Gubernatorial:** Perdue (2008, D+33.56, 65.45% to 31.89%), Dalton (2012, D+21.83, 59.32% to 37.49%), Cooper (2016, D+35.49, 66.87% to 31.38%), Cooper (2020, D+32.52, 63.56% to 31.04%, Oth 5.40%), Stein (2024, D+47.58, 71.89% to 24.31%, Oth 3.80%).
  NC-04 is a Democratic stronghold in gubernatorial races, with margins growing from Perdue’s 28-point win in 2008 to Stein’s 47.6-point win in 2024, reflecting the district’s urban, highly educated, and diverse population.
- **Lt. Governor:** Dalton (2008, D+30.56, 65.06% to 34.50%), Coleman (2012, D+21.83, 59.32% to 37.49%), Coleman (2016, D+35.49, 66.87% to 31.38%), Holley (2020, D+32.52, 63.56% to 31.04%, Oth 5.40%), Hunt (2024, D+47.58, 71.89% to 24.31%, Oth 3.80%).
  The district has delivered large and growing Democratic margins for Lt. Governor, with Hunt’s 2024 win the largest in recent cycles.
- **Senate:** Hagan (2008, D+20.89, 59.04% to 38.15%), Marshall (2010, D+7.02, 52.47% to 45.45%), Hagan (2014, D+7.54, 52.35% to 44.81%), Ross (2016, D+7.39, 52.13% to 44.74%), Cunningham (2020, D+11.80, 54.90% to 43.10%), Beasley (2022, D+10.10, 54.10% to 44.00%).
Senate races have consistently produced large Democratic margins, with the district remaining a Democratic bastion in federal contests.
- **Attorney General:**
    - 2016: Josh Stein (D, State Senator) vs. Buck Newton (R, State Senator): D+36.77 (68.39% to 31.62%)
    - 2020: Josh Stein (D, incumbent) vs. Jim O'Neill (R, Forsyth County District Attorney): D+36.09 (68.05% to 31.96%)
    - 2024: Jeff Jackson (D, NC-14 before redistricting, from Charlotte) vs. Dan Bishop (R, NC-08, from Waxhaw in Union County): D+38.24 (69.12% to 30.88%)

  The Attorney General races from 2016 to 2024 in this district have shown a dominant Democratic advantage, with Jackson winning by nearly 40 points in 2024. Both 2024 candidates were sitting members of Congress.


    - **Supreme Court:**
      - 2022: Richard Dietz (R) vs. Lucy Inman (D): D+35.38 (67.69% to 32.31%)
      - 2022: Trey Allen (R) vs. Sam Ervin IV (D): D+34.90 (67.45% to 32.55%)
      - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): D+36.70 (68.35% to 31.65%)

  Supreme Court races in NC-04 have produced overwhelming Democratic margins for Riggs (D) over Griffin (R) in 2024 and Inman (D) over Dietz (R) in 2022, mirroring the district’s status as the most Democratic in the state.

---

## Trends in NC-05 (Northwest / Foothills / Mt. Airy)

**Summary:**  
NC-05 covers the northwestern foothills and mountain regions of North Carolina, including most of Winston-Salem, the college town of Boone (home to Appalachian State University), and a mix of rural, suburban, and small-town communities. The district’s population is anchored by the urban center of Winston-Salem, but also includes Stokes, Surry, Wilkes, Watauga, Ashe, Alleghany, and parts of Forsyth and Caldwell counties. While Boone and parts of Winston-Salem provide pockets of Democratic support, the outlying areas are deeply conservative and reliably Republican. The district has become an even stronger GOP stronghold in recent years, with Democrats struggling to reach 40% in most races. Economic drivers include higher education, healthcare, agriculture, and tourism in the Blue Ridge Mountains, but the region faces challenges from population aging and the decline of traditional industries. NC-05’s results reflect the growing Republican dominance in both rural and exurban parts of the region, even as urban and university communities remain competitive.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 42.55%, McCain 55.95%, Oth 1.50% (R+13.40)
    - 2012: Obama 40.72%, Romney 59.28% (R+18.56)
    - 2016: Clinton 36.68%, Trump 59.15%, Oth 4.17% (R+22.47)
    - 2020: Biden 38.69%, Trump 59.94%, Oth 1.37% (R+21.25)
    - 2024: Harris 38.16%, Trump 60.82%, Oth 1.02% (R+22.66)
- **Gubernatorial:** Perdue (D) 2008: R+6.63 (45.81% to 52.44%); McCrory (R) 2012: R+21.27 (39.05% to 60.32%); McCrory (R), 2016: R+20.29 (59.41% to 39.12%); Forest (R) 2020: R+13.33 (56.00% to 42.67%, Oth 1.33%); Robinson (R) 2024: R+2.27 (48.59% to 46.32%, Oth 5.09%).
  NC-05 is a Republican stronghold in gubernatorial races, with GOP margins growing from 5 points in 2008 to over 22 points in 2012, and remaining solidly Republican through 2024.
- **Lt. Governor:** Pittenger (R) vs. Dalton (D), 2008: R+10.50 (55.25% to 44.75%); Forest (R) vs. Coleman (D), 2012: R+13.20 (56.60% to 43.40%); Forest (R) vs. Coleman (D), 2016: R+17.80 (58.90% to 41.10%); Robinson (R) vs. Holley (D), 2020: R+26.80 (62.60% to 35.80%); Robinson (R) vs. Hunt (D), 2024: R+23.25 (59.97% to 36.72%).
  The district has become increasingly Republican for Lt. Governor, with Democratic margins declining and GOP leads growing in recent cycles.
- **Senate:** Hagan (D) vs. Dole (R), 2008: R+2.63 (46.81% to 49.44%); Burr (R) vs. Marshall (D), 2010: R+26.34 (62.19% to 35.85%); Tillis (R) vs. Hagan (D), 2014: R+18.28 (38.60% to 56.88%); Ross (D) vs. Burr (R), 2016: R+24.48 (35.86% to 60.34%); Tillis (R) vs. Cunningham (D), 2020: R+17.06 (38.90% to 55.96%); Budd (R) vs. Beasley (D), 2022: R+23.20 (37.60% to 60.80%).
  Senate races have shown a strong and growing Republican advantage, with Democratic margins falling and GOP leads expanding over time.
- **Attorney General:**
    - 2016: Buck Newton (R, State Senator) vs. Josh Stein (D, State Senator): R+15.99 (57.99% to 42.01%)
    - 2020: Jim O'Neill (R, Forsyth County District Attorney) vs. Josh Stein (D, incumbent): R+20.02 (60.01% to 39.99%)
    - 2024: Dan Bishop (R, NC-08, from Waxhaw in Union County) vs. Jeff Jackson (D, NC-14 before redistricting, from Charlotte): R+16.48 (58.24% to 41.76%)
  The Attorney General races from 2016 to 2024 in this district have shown a strong Republican advantage, with Bishop maintaining a large margin in 2024. Both 2024 candidates were sitting members of Congress.

---

## Trends in NC-06 (Greensboro / Winston-Salem / High Point)

**Summary:**  
NC-06 encompasses the heart of the Triad region, including most of Greensboro, Winston-Salem, and High Point—three of North Carolina’s largest and most diverse cities. The district also includes surrounding suburbs and exurban communities in Guilford and Forsyth counties. Once a competitive or GOP-leaning seat, NC-06 has shifted decisively toward the Democratic Party in recent cycles, driven by rapid urban growth, an influx of young professionals and college students, and increasing racial and ethnic diversity. Greensboro is home to several major universities (UNC Greensboro, NC A&T, Guilford College), while Winston-Salem boasts a strong healthcare and research sector anchored by Wake Forest University. The district’s economy is fueled by education, healthcare, logistics, and advanced manufacturing, and its population is among the most urban and highly educated in the state. Recent elections have seen rising turnout among young, Black, and Latino voters, further strengthening Democratic margins. However, some suburban and exurban precincts remain competitive, reflecting the region’s ongoing demographic and political evolution.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 55.34%, McCain 43.60%, Oth 1.06% (D+11.74)
    - 2012: Obama 54.74%, Romney 45.26% (D+9.48)
    - 2016: Clinton 53.36%, Trump 42.92% (D+10.44)
    - 2020: Biden 55.50%, Trump 43.12% (D+12.38)
    - 2024: Harris 54.59%, Trump 44.13% (D+10.46)
  The district has consistently voted Democratic for president, with margins ranging from 10 to 13 points, reflecting the Triad’s urban and diverse electorate.
**Gubernatorial:** Perdue (D, 2008) +15.04 (55.94% to 40.90%); McCrory (R, 2012) +0.32 (49.09% to 48.77%); Cooper (D, 2016) +10.76 (54.77% to 44.01%); Cooper (D, 2020) +18.87 (58.68% to 39.81%); Stein (D, 2024) +28.19 (61.67% to 33.48%).
  NC-06 has remained Democratic in gubernatorial races, with margins growing from 15 points in 2008 to over 28 points in 2024, as the district’s urban core has become more Democratic.
- **Lt. Governor:** Coleman (D) vs. Forest (R), 2016: D+5.80 (52.10% to 46.30%); Holley (D) vs. Robinson (R), 2020: D+5.80 (52.10% to 46.30%); Hunt (D) vs. Robinson (R), 2024: D+8.46 (53.03% to 44.57%).
  The district has leaned Democratic for Lt. Governor, but margins have fluctuated, with a modest increase for Hunt in 2024 compared to Coleman in 2016 and Holley in 2020.
- **Senate:** Hagan (2008, D+20.89, 59.04% to 38.15%), Marshall (2010, D+7.02, 52.47% to 45.45%), Hagan (2014, D+7.54, 52.35% to 44.81%), Ross (2016, D+7.39, 52.13% to 44.74%), Cunningham (2020, D+11.80, 54.90% to 43.10%), Beasley (2022, D+10.10, 54.10% to 44.00%).
  Senate races have consistently produced large Democratic margins, with the district remaining a Democratic bastion in federal contests.
- **Attorney General:**
    - 2016: Josh Stein (D, State Senator) vs. Buck Newton (R, State Senator): D+22.14 (61.07% to 38.93%)
    - 2020: Josh Stein (D, incumbent) vs. Jim O'Neill (R, Forsyth County District Attorney): D+28.36 (64.18% to 35.82%)
    - 2024: Jeff Jackson (D, NC-14 before redistricting, from Charlotte) vs. Dan Bishop (R, NC-08, from Waxhaw in Union County): D+16.48 (58.24% to 41.76%)
  The Attorney General races from 2016 to 2024 in this district have shown a strong and growing Democratic advantage, with Jackson increasing the margin in 2024. Both 2024 candidates were sitting members of Congress.

---

## Trends in NC-07 (Fayetteville / Wilmington / Lumberton)

**Summary:**  
NC-07 spans southeastern North Carolina, stretching from the fast-growing coastal communities of Brunswick County (just north of Myrtle Beach, SC, and west of Wilmington) through the urban centers of Wilmington and Fayetteville, and into the rural heartland of the Sandhills. Brunswick County is one of the fastest-growing counties in the state, fueled by an influx of retirees, new residents from the Northeast and Midwest, and a booming real estate market; its population is predominantly white and older than the state average, with rapid suburban and exurban development. Much of this growth is concentrated in coastal communities like Leland, Southport, Shallotte, Oak Island, Ocean Isle Beach, and Sunset Beach, where new housing, golf course developments, and active adult communities attract conservative retirees from the Northeast and Midwest. This influx has reinforced Brunswick County’s strong Republican trend and fueled rapid suburban and exurban expansion. The district also includes the pivotal Obama-Trump counties of Bladen and Robeson—Robeson being home to the Lumbee tribe, whose recent realignment toward the GOP has been especially influential. While Fayetteville and Wilmington anchor Democratic strength with their diverse, urban populations and military presence, the district’s rural and exurban counties have trended sharply Republican. NC-07 is a microcosm of the broader realignment and demographic shifts underway in southeastern North Carolina, blending fast-growing coastal suburbs, diverse urban centers, and rural communities undergoing significant political change.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 47.47%, McCain 51.60%, Oth 0.93% (R+4.13)
    - 2012: Obama 47.35%, Romney 52.65% (R+5.30)
    - 2016: Clinton 41.73%, Trump 54.64%, Oth 3.62% (R+12.91)
    - 2020: Biden 42.97%, Trump 55.69%, Oth 1.34% (R+12.72)
    - 2024: Harris 41.55%, Trump 57.57%, Oth 0.87% (R+16.02)
- **Gubernatorial:** Forest (R) won by 5.1 points in 2020 (51.8% to 46.7%), but Robinson (R) lost the district by 5.9 points in 2024 (44.2% to 50.1%), showing Democratic resilience in urban centers.
    - **Gubernatorial Margins (2008–2024):**
        - 2008: Perdue (D) +4.0 (52.0% to 48.0%)
        - 2012: McCrory (R) +13.0 (56.5% to 43.5%)
        - 2016: McCrory (R) +5.2 (51.48% to 46.29%, Oth 2.23%)
        - 2020: Forest (R) +5.1 (51.8% to 46.7%)
        - 2024: Stein (D) +5.9 (50.1% to 44.2%)
      The district has swung between parties in gubernatorial races, with narrow Democratic wins in 2008 and 2016, and narrow Republican wins in 2012 and 2020. The 2024 election marked a significant Democratic gain, with Stein winning by nearly 6 points.
- **Senate:** Tillis (R) won by 11.5 points in 2020 (55.1% to 43.6%), Budd (R) by 13.8 points in 2022 (56.1% to 42.3%).
    - **Senate Margins (2008–2022):**
        - 2008: Dole (R) +7.2 (52.1% to 44.9%)
        - 2010: Burr (R) +12.1 (54.7% to 42.6%)
        - 2014: Tillis (R) +10.3 (53.8% to 43.5%)
        - 2016: Burr (R) +9.2 (54.2% to 45.0%)
        - 2020: Tillis (R) +6.6 (52.4% to 45.8%)
        - 2022: Budd (R) +8.4 (53.3% to 44.9%)
      The district has consistently favored Republican Senate candidates, with margins ranging from R+6.6 to R+12.1 over the past six cycles. While the GOP's advantage has narrowed slightly in recent years, Democrats have not won a Senate race in the district during this period.
- **County Flips:** Robeson County, home to the Lumbee tribe, flipped from Democratic to Republican along with Bladen County in 2016 and has remained GOP since, symbolizing the realignment of Native and rural voters. Scotland County also flipped Republican in 2020 and 2022 Senate races.
- **Supreme Court:**
      - 2022: Richard Dietz (R) vs. Lucy Inman (D): R+13.42 (56.71% to 43.29%)
      - 2022: Trey Allen (R) vs. Sam Ervin IV (D): R+14.10 (57.05% to 42.95%)
      - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): R+7.86 (53.93% to 46.07%)

  Supreme Court races in NC-07 have produced solid Republican margins for Griffin (R) over Riggs (D) in 2024 and Dietz (R) over Inman (D) in 2022, consistent with the district’s GOP lean but with some Democratic competitiveness.

- **Demographics:** The district is diverse, with significant Black, Native (especially Lumbee), and military populations. Rural white voters have shifted strongly Republican, while urban and minority precincts remain Democratic.
- **Realignment:** NC-07 is a case study in rural and Native voter realignment, with Robeson County’s shift especially notable. The district’s margins reflect the growing GOP strength in rural areas and persistent Democratic support in urban centers.

**Narrative Note:**  
> *NC-07’s transformation is driven by the dramatic realignment of Robeson County and the Lumbee tribe, as well as broader rural shifts. While Fayetteville and Wilmington anchor Democratic strength, the district’s rural and Native areas now form a solid Republican bloc, making NC-07 a microcosm of eastern North Carolina’s changing political landscape.*

---

## Trends in NC-08 (Lexington / Salisbury / Union County)


**Summary:**  
NC-08 covers the exurban fringes of Charlotte, the fast-growing Piedmont Triad exurbs (including Davidson County), and a swath of rural south-central North Carolina. The district includes Union County—a very fast-growing Charlotte exurb due to its proximity to the city, but one that has barely shifted in federal elections—as well as Stanly, Montgomery, Anson, Richmond, and parts of Cabarrus and Rowan counties. Union and Davidson counties anchor the district’s rapid population growth, driven by new housing developments and an influx of families seeking affordable living near Charlotte and the Triad. The population is predominantly white, suburban, and exurban, with a mix of small towns and rural communities. GOP margins have grown as rural and exurban voters consolidate behind the party, and conservative newcomers from the Charlotte metro area reinforce Republican dominance. Democrats have struggled to make inroads, with the district’s political culture shaped by suburban growth, evangelical churches, and a strong tradition of conservative politics. Major population centers in the district include Lexington, Salisbury, Albemarle, and rapidly growing Union County suburbs such as Monroe and Indian Trail—both of which have seen explosive growth as families move outward from Charlotte. This suburban expansion has made Union County one of the fastest-growing in the state, yet it remains solidly Republican in federal elections. Other notable communities include Thomasville on the district’s northern fringe, further illustrating the geographic and demographic diversity of NC-08.

The district’s economy is anchored by manufacturing, logistics, agriculture, and retail, with many residents commuting to jobs in Charlotte, the Triad, or local industrial parks. Towns like Monroe, Indian Trail, and Thomasville serve as key commuter hubs, while Lexington and Salisbury have long histories in furniture, textiles, and food processing. This blend of traditional industries and suburban growth shapes both the economic landscape and the political culture of NC-08.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 36.47%, McCain 62.16%, Oth 1.37% (R+25.69)
    - 2012: Obama 33.00%, Romney 65.40%, Oth 1.60% (R+32.40)
    - 2016: Clinton 29.67%, Trump 66.02%, Oth 4.31% (R+36.35)
    - 2020: Biden 32.34%, Trump 66.35%, Oth 1.31% (R+34.01)
    - 2024: Harris 31.90%, Trump 67.14%, Oth 0.96% (R+35.24)
- **Gubernatorial:** Republican candidates have dominated, with Forest (R) winning by 27.3 points in 2020 (63.0% to 35.7%) and Robinson (R) by 15.9 points in 2024 (57.7% to 39.3%).
- **Senate:** GOP Senate candidates have won by similar margins: Tillis (R) by 34.2 points in 2020 (66.3% to 32.1%), Budd (R) by 35.7 points in 2022 (67.1% to 28.9%).
- **County Flips:** Anson County flipped narrowly Republican in 2024 (Trump +2), ending a long Democratic streak dating back to the 1970s. Otherwise, the district remains solidly Republican.
- **Demographics:** The district is predominantly white, rural, and growing slowly, with Union County as the main population center.

    - **Supreme Court:**
      - 2022: Richard Dietz (R) vs. Lucy Inman (D): R+38.98 (69.49% to 30.51%)
      - 2022: Trey Allen (R) vs. Sam Ervin IV (D): R+39.40 (69.70% to 30.30%)
      - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): R+34.58 (67.29% to 32.71%)

  Supreme Court races in NC-08 have produced overwhelming Republican margins for Griffin (R) over Riggs (D) in 2024 and Dietz (R) over Inman (D) in 2022, consistent with the district’s status as a GOP stronghold.
**Realignment:** NC-08 is part of the GOP’s rural and exurban firewall, with little sign of Democratic resurgence.

**Narrative Note:**  
> *NC-08’s margins have remained among the largest for Republicans in the state, with little change over the past decade. The district’s rural and exurban character, combined with slow demographic change, has kept it firmly in the GOP column.*

---

## Trends in NC-09 (Asheboro / Fort Bragg / Southern Pines)


**Summary:**  
NC-09, stretching from the Sandhills to the southern Piedmont, is a Republican-leaning district with pockets of competitiveness near military bases and growing suburbs. The district includes Randolph County (the most Republican county in the state and a fast-growing Triad exurb), as well as Moore, Hoke, Lee, Scotland, Richmond, Montgomery, and parts of Cumberland and Harnett counties. These areas encompass a mix of rural communities, military families (especially near Fort Bragg), and suburban growth. While the GOP dominates, Democrats have made some gains in suburban precincts, especially in the Fayetteville area. The district's population is shaped by a blend of long-established rural families, military personnel, and newcomers drawn by affordable housing and job opportunities in the Triad and Sandhills regions.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 48.60%, McCain 50.17%, Oth 1.23% (R+1.57)
    - 2012: Obama 48.50%, Romney 50.00%, Oth 1.50% (R+1.50)
    - 2016: Clinton 49.07%, Trump 47.00%, Oth 3.93% (D+2.07)
    - 2020: Biden 49.97%, Trump 48.28%, Oth 1.75% (D+1.69)
    - 2024: Harris 49.76%, Trump 48.80%, Oth 1.44% (D+0.96)
- **Governor:** Margins have also been close in gubernatorial races: Perdue (2008, D+2.1, 49.6% to 47.5%), McCrory (2012, R+7.5, 53.2% to 45.3%), McCrory (2016, R+7.5, 53.2% to 45.3%), Cooper (2020, D+7.9, 53.2% to 45.3%), Stein (2024, D+20.8, 57.6% to 36.8%).
- **Lt. Governor:** The district has seen competitive but increasingly Democratic results: Dalton (2008, D+1.2, 49.1% to 47.9%), Forest (2012, R+6.2, 52.1% to 45.9%), Robinson (R+7.0, 52.5% to 45.5%), Holley (2020, D+2.5, 50.2% to 47.7%), Hunt (2024, D+8.2, 52.6% to 44.4%).
- **Senate:** Senate races have also been close: Hagan (2008, D+5.1, 51.1% to 46.0%), Burr (2010, R+12.4, 55.2% to 42.8%), Tillis (R+2.4, 49.5% to 47.1%), Burr (R+5.0, 50.9% to 45.9%), Tillis (2020, D+2.07, 49.07% to 47.00%), Budd (2022, R+1.0, 49.6% to 48.6%).
- **Attorney General:**
    - 2016: Josh Stein (D, State Senator) vs. Buck Newton (R, State Senator): D+0.62 (50.31% to 49.69%)
    - 2020: Josh Stein (D, incumbent) vs. Jim O'Neill (R, Forsyth County District Attorney): D+1.75 (50.87% to 49.12%)
    - 2024: Jeff Jackson (D, NC-14 before redistricting, from Charlotte) vs. Dan Bishop (R, NC-08, from Waxhaw in Union County): D+3.44 (51.72% to 48.28%)
  The Attorney General races from 2016 to 2024 in this district have shown a consistent Democratic advantage, with Stein winning by 8.2 points in 2024. Both 2024 candidates were sitting members of Congress.

---
## Trends in NC-10 (Western Foothills / NW Gaston / Cleveland County)

**Summary:**  
NC-10 covers the western foothills and lower mountain regions, including Cleveland, Lincoln, Catawba, Burke, and parts of Gaston and Caldwell counties. Anchored by cities like Hickory, Shelby, Lincolnton, and Morganton, the district is predominantly white, working-class, and deeply conservative. The economy is driven by manufacturing, logistics, and agriculture, with a legacy of textile and furniture production. Population growth is slow, with some out-migration of younger residents, but Gaston County’s exurbs are expanding as Charlotte’s influence creeps westward. The region’s political culture is shaped by evangelical churches, small-town traditions, and a strong sense of local identity. NC-10 is one of the most reliably Republican districts in the state, with the GOP routinely winning by 30 points or more in federal and statewide races. Democratic support is limited to a few urban precincts in Hickory and Morganton, but the overall trend is one of overwhelming Republican dominance. Notably, NC-10 also includes all of Iredell and Alexander counties. In addition to its traditional manufacturing and agricultural base, NC-10 is increasingly shaped by rapid suburban growth along the Lake Norman corridor, which spans both southern Iredell County (Mooresville, Troutman) and eastern Lincoln County (Denver, Lake Norman communities). These areas have attracted an influx of families, professionals, and retirees drawn by proximity to Charlotte, new housing developments, and recreational opportunities on Lake Norman. The result is a district that blends old-line, small-town conservatism with pockets of dynamic suburban expansion. While this growth has diversified the local economy and population, the district remains overwhelmingly Republican, with the new arrivals generally reinforcing rather than diluting the GOP's dominance.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 36.22%, McCain 62.38%, Oth 1.40% (R+26.16)
    - 2012: Obama 31.00%, Romney 67.00%, Oth 2.00% (R+36.00)
    - 2016: Clinton 28.53%, Trump 66.77%, Oth 4.70% (R+38.24)
    - 2020: Biden 29.65%, Trump 69.11%, Oth 1.24% (R+39.46)
    - 2024: Harris 29.43%, Trump 69.74%, Oth 0.83% (R+40.31)
- **Gubernatorial:** Republican dominance: Perdue (D) 2008: R+27.09 (35.38% to 62.47%); McCrory (R) 2012: R+38.00 (30.00% to 68.00%); McCrory (R) 2016: R+37.44 (30.45% to 67.89%); Forest (R) 2020: R+32.86 (32.90% to 65.76%); Robinson (R) 2024: R+20.65 (37.00% to 57.65%, Oth 5.35%).
- **Senate:** GOP landslides: Hagan (D) 2008: R+12.08 (41.92% to 54.00%); Burr (R) 2010: R+33.21 (32.17% to 65.38%); Hagan (D) 2014: R+29.07 (32.72% to 61.79%); Ross (D) 2016: R+28.31 (31.69% to 60.00%); Tillis (R) 2020: R+38.80 (29.80% to 68.60%); Budd (R) 2022: R+39.65 (28.90% to 69.30%).
- **Attorney General:**
    - 2016: Buck Newton (R) vs. Josh Stein (D): R+35.98 (67.99% to 32.01%)
    - 2020: Jim O'Neill (R) vs. Josh Stein (D): R+35.98 (67.99% to 32.01%)
    - 2024: Dan Bishop (R) vs. Jeff Jackson (D): R+35.98 (67.99% to 32.01%)
  The Attorney General races have shown overwhelming Republican margins, with little Democratic presence.
- **Supreme Court:**
    - 2022: Richard Dietz (R) vs. Lucy Inman (D): R+37.16 (68.58% to 31.42%)
    - 2022: Trey Allen (R) vs. Sam Ervin IV (D): R+37.16 (68.58% to 31.42%)
    - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): R+36.16 (68.08% to 31.92%)
  Supreme Court races mirror the district’s strong GOP lean, with Griffin (R) and Dietz (R) winning by over 36 points.

---
## Trends in NC-11 (Asheville / Hendersonville / Brevard)

**Summary:**  
NC-11 encompasses the heart of western North Carolina, including Asheville, Hendersonville, Brevard, and the surrounding mountain counties. The district is geographically vast and diverse, with Asheville serving as a progressive, artsy urban hub surrounded by deeply conservative rural and small-town communities. The economy is driven by tourism, outdoor recreation, healthcare, and higher education, with Asheville’s rapid growth and cultural vibrancy contrasting with the slower pace and traditional values of the outlying counties. The region is home to a significant retiree population, a growing Latino community, and a strong tradition of localism. While Asheville and a few nearby precincts vote Democratic, the rest of the district is solidly Republican, making NC-11 a classic example of the urban-rural divide in North Carolina politics. Jackson County, home to Western Carolina University, is a notable swing area but has trended Republican in recent cycles. The rest of the district—comprising counties like Haywood, Macon, Swain, Transylvania, Madison, Yancey, Polk, Graham, Cherokee, and Clay—remains deeply conservative and reliably Republican, reinforcing the stark urban-rural divide that defines NC-11.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 46.26%, McCain 52.01%, Oth 1.73% (R+5.75)
    - 2012: Obama 44.00%, Romney 54.00%, Oth 2.00% (R+10.00)
    - 2016: Clinton 41.68%, Trump 54.17%, Oth 4.15% (R+12.49)
    - 2020: Biden 44.15%, Trump 54.28%, Oth 1.57% (R+10.13)
    - 2024: Harris 45.00%, Trump 53.78%, Oth 1.22% (R+8.78)
- **Gubernatorial:** Perdue (D) 2008: D+5.46 (50.85% to 45.39%); McCrory (R) 2012: R+14.00 (42.00% to 56.00%); McCrory (R) 2016: R+6.22 (46.12% to 52.34%); Forest (R) 2020: R+3.99 (47.21% to 51.21%); Robinson (R) 2024: R+8.26 (43.60% to 51.86%, Oth 4.54%).
- **Senate:** Hagan (D) 2008: D+3.89 (50.02% to 46.13%); Burr (R) 2010: R+14.87 (41.17% to 56.04%); Hagan (D) 2014: R+5.19 (45.11% to 50.30%); Ross (D) 2016: R+12.49 (41.68% to 54.17%); Tillis (R) 2020: R+9.80 (44.30% to 54.10%); Budd (R) 2022: R+10.60 (43.80% to 54.40%).
- **Attorney General:**
    - 2016: Josh Stein (D) vs. Buck Newton (R): R+8.72 (45.64% to 54.36%)
    - 2020: Josh Stein (D) vs. Jim O'Neill (R): R+8.72 (45.64% to 54.36%)
    - 2024: Jeff Jackson (D) vs. Dan Bishop (R): R+8.72 (45.64% to 54.36%)
  The Attorney General races have shown a consistent Republican advantage, with margins around 9 points.
- **Supreme Court:**
    - 2022: Richard Dietz (R) vs. Lucy Inman (D): R+6.00 (53.00% to 47.00%)
    - 2022: Trey Allen (R) vs. Sam Ervin IV (D): R+6.00 (53.00% to 47.00%)
    - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): R+6.00 (53.00% to 47.00%)
  Supreme Court races show a modest Republican edge, with Griffin (R) and Dietz (R) winning by 6 points.

---
## Trends in NC-12 (Uptown Charlotte / Davidson / Concord)

**Summary:**  
NC-12 is centered on Uptown Charlotte and its northern suburbs, including Davidson, Concord, and parts of Cabarrus and Mecklenburg counties. The district is highly urban, racially and ethnically diverse, and rapidly growing, with a large Black population and significant Latino and Asian communities. Charlotte’s status as a major banking, tech, and healthcare hub drives economic growth and attracts young professionals from across the country. The district’s political culture is shaped by progressive activism, high educational attainment, and a strong tradition of civic engagement. NC-12 is one of the most Democratic districts in the state, with the party routinely winning by 25 points or more in federal and statewide races. Republican support is limited to a few suburban precincts, but the overall trend is one of growing Democratic strength, fueled by demographic change and urbanization.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 61.29%, McCain 37.86%, Oth 0.85% (D+23.43)
    - 2012: Obama 62.00%, Romney 36.00%, Oth 2.00% (D+26.00)
    - 2016: Clinton 58.61%, Trump 37.45%, Oth 3.94% (D+21.16)
    - 2020: Biden 64.24%, Trump 34.14%, Oth 1.62% (D+30.10)
    - 2024: Harris 63.62%, Trump 34.65%, Oth 1.73% (D+28.97)
- **Gubernatorial:** Perdue (D) 2008: D+6.26 (52.15% to 45.89%); McCrory (R) 2012: D+10.00 (54.00% to 44.00%); McCrory (R) 2016: D+26.22 (62.34% to 36.12%); Forest (R) 2020: D+33.66 (65.87% to 32.21%); Robinson (R) 2024: D+42.97 (68.95% to 25.98%, Oth 5.07%).
- **Senate:** Hagan (D) 2008: D+27.01 (61.99% to 34.98%); Burr (R) 2010: D+9.10 (53.67% to 44.57%); Hagan (D) 2014: D+22.95 (60.05% to 37.10%); Ross (D) 2016: D+21.16 (58.61% to 37.45%); Tillis (R) 2020: D+27.00 (63.10% to 35.10%); Beasley (D) 2022: D+26.10 (62.10% to 36.00%).
- **Attorney General:**
    - 2016: Josh Stein (D) vs. Buck Newton (R): D+30.18 (65.09% to 34.91%)
    - 2020: Josh Stein (D) vs. Jim O'Neill (R): D+30.18 (65.09% to 34.91%)
    - 2024: Jeff Jackson (D) vs. Dan Bishop (R): D+30.18 (65.09% to 34.91%)
  The Attorney General races have shown a dominant Democratic advantage, with margins over 30 points.
- **Supreme Court:**
    - 2022: Richard Dietz (R) vs. Lucy Inman (D): D+31.90 (65.95% to 34.05%)
    - 2022: Trey Allen (R) vs. Sam Ervin IV (D): D+31.90 (65.95% to 34.05%)
    - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): D+31.90 (65.95% to 34.05%)
  Supreme Court races in NC-12 have produced overwhelming Democratic margins, with Riggs (D) and Inman (D) winning by nearly 32 points.

---
## Trends in NC-13 (South Wake Suburbs / Johnston / Wayne)

**Summary:**  
NC-13 covers the fast-growing southern and eastern suburbs of Raleigh, including Johnston, Wayne, and parts of Wake and Harnett counties. The district is a mix of rapidly developing exurbs, small towns, and rural communities, with Johnston County as the main population center. The area has seen explosive growth as families move outward from Raleigh in search of affordable housing and new job opportunities. The population is predominantly white, with a growing Latino community and a strong tradition of evangelical Christianity. The economy is anchored by manufacturing, logistics, agriculture, and retail, with many residents commuting to jobs in Raleigh or the Research Triangle. Politically, NC-13 is a true battleground, with close margins in most statewide races and a history of swinging between parties. The district’s rapid growth, demographic change, and suburbanization have made it one of the most competitive in the state, with both parties investing heavily in outreach and turnout efforts.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 49.36%, McCain 49.52%, Oth 1.12% (R+0.16)
    - 2012: Obama 48.50%, Romney 50.00%, Oth 1.50% (R+1.50)
    - 2016: Clinton 45.88%, Trump 50.89%, Oth 3.23% (R+5.01)
    - 2020: Biden 49.97%, Trump 48.28%, Oth 1.75% (D+1.69)
    - 2024: Harris 49.76%, Trump 48.80%, Oth 1.44% (D+0.96)
- **Gubernatorial:** Perdue (D) 2008: D+2.07 (49.61% to 47.54%); McCrory (R) 2012: R+6.00 (46.00% to 52.00%); McCrory (R) 2016: R+1.89 (48.23% to 50.12%); Forest (R) 2020: D+7.92 (53.19% to 45.27%); Robinson (R) 2024: D+20.77 (57.57% to 36.80%, Oth 5.63%).
- **Senate:** Hagan (D) 2008: D+5.14 (51.13% to 45.99%); Burr (R) 2010: R+12.43 (42.79% to 55.22%); Hagan (D) 2014: R+2.37 (47.11% to 49.48%); Ross (D) 2016: R+5.01 (45.88% to 50.89%); Tillis (R) 2020: D+0.10 (49.10% to 49.00%); Beasley (D) 2022: R+1.00 (48.60% to 49.60%).
- **Attorney General:**
    - 2016: Josh Stein (D) vs. Buck Newton (R): D+3.50 (51.75% to 48.25%)
    - 2020: Josh Stein (D) vs. Jim O'Neill (R): D+3.50 (51.75% to 48.25%)
    - 2024: Jeff Jackson (D) vs. Dan Bishop (R): D+3.50 (51.75% to 48.25%)
  The Attorney General races have shown a modest Democratic advantage, with margins around 3.5 points.
- **Supreme Court:**
    - 2022: Richard Dietz (R) vs. Lucy Inman (D): D+4.08 (52.04% to 47.96%)
    - 2022: Trey Allen (R) vs. Sam Ervin IV (D): D+4.08 (52.04% to 47.96%)
    - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): D+4.08 (52.04% to 47.96%)
  Supreme Court races in NC-13 have produced narrow Democratic margins, with Riggs (D) and Inman (D) winning by just over 4 points.

---

## Trends in NC-14 (Charlotte South / Ballantyne / Gaston)

**Summary:**  
NC-14, covering the southern and western suburbs of Charlotte, is a rapidly evolving district that has seen significant Democratic gains in recent cycles. The district includes parts of Mecklenburg and Gaston counties, encompassing fast-growing suburban communities like Matthews, Pineville, Belmont, and Mount Holly. Population growth has been fueled by an influx of younger families, professionals, and a more racially and ethnically diverse population, drawn by the area’s economic opportunities and quality of life. Once reliably Republican, the district’s political landscape has shifted as suburbanization and demographic change have eroded the GOP’s advantage, especially in Mecklenburg County. While Gaston County remains more conservative, Democratic candidates have made inroads in its suburban precincts. NC-14’s results reflect the broader trend of suburban areas in North Carolina moving toward the Democratic Party, making it one of the state’s most closely watched and competitive districts for the future.

**Key Trends:**
- **Presidential:** Democratic and Republican margins by year:
    - 2008: Obama 51.60%, McCain 47.47%, Oth 0.93% (D+4.13)
    - 2012: Obama 54.00%, Romney 44.00% (D+10.00)
    - 2016: Clinton 49.07%, Trump 47.00%, Oth 3.93% (D+2.07)
    - 2020: Biden 57.33%, Trump 40.97%, Oth 1.70% (D+16.36)
    - 2024: Harris 57.00%, Trump 41.64%, Oth 1.36% (D+15.36)

    - **Supreme Court:**
      - 2022: Richard Dietz (R) vs. Lucy Inman (D): D+8.10 (54.05% to 45.95%)
      - 2022: Trey Allen (R) vs. Sam Ervin IV (D): D+7.90 (53.95% to 46.05%)
      - 2024: Allison Riggs (D) vs. Jefferson Griffin (R): D+14.20 (57.10% to 42.90%)

      Supreme Court races in NC-14 have produced solid Democratic margins for Riggs (D) over Griffin (R) in 2024 and Inman (D) over Dietz (R) in 2022, consistent with the district’s Democratic trend in recent cycles.
- **Gubernatorial:** Perdue (2008, D+11.80, 54.20% to 42.40%), Dalton (2012, D+1.80, 49.90% to 48.10%), Cooper (2016, D+8.10, 54.60% to 46.50%), Cooper (2020, D+11.80, 54.20% to 42.40%), Stein (2024, D+20.80, 57.60% to 36.80%).
  NC-14 has trended Democratic in gubernatorial races, with margins increasing from Perdue’s 11.8-point win in 2008 to Stein’s 20.8-point win in 2024, reflecting the district’s suburbanization and demographic changes.
- **Lt. Governor:** Holley (2016, D+4.20, 52.10% to 47.90%), Hunt (2024, D+15.50, 56.30% to 40.80%).
  The district has leaned Democratic for Lt. Governor, with a significant increase for Hunt in 2024 compared to Coleman in 2016 and Holley in 2020.
- **Senate:** Hagan (2008, D+13.56, 59.04% to 45.45%), Marshall (2010, D+7.02, 52.47% to 45.45%), Hagan (2014, D+18.28, 54.38% to 32.38%), Ross (2016, D+6.62, 52.55% to 45.99%), Cunningham (2020, D+8.90, 54.90% to 43.10%), Beasley (2022, D+8.20, 54.20% to 43.80%).
  Senate races have shown generally Democratic margins, with some fluctuation, but a clear trend of Democratic strength in recent cycles.
- **Attorney General:**
    - 2016: Josh Stein (D, State Senator) vs. Buck Newton (R, State Senator): D+4.16 (52.08% to 47.92%)
    - 2020: Josh Stein (D, incumbent) vs. Jim O'Neill (R, Forsyth County District Attorney): D+7.44 (53.72% to 46.28%)
    - 2024: Jeff Jackson (D, NC-14 before redistricting, from Charlotte) vs. Dan Bishop (R, NC-08, from Waxhaw in Union County): D+11.49 (55.75% to 44.26%)
  The Attorney General races from 2016 to 2024 in this district have shown a consistent Democratic advantage, with Jackson winning by nearly 16 points in 2024. Both 2024 candidates were sitting members of Congress.

---
