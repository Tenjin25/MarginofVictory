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

--

## District-Level 2008 Gubernatorial Results

| District | Region                                   | Perdue (D) % | McCrory (R) % |
|----------|------------------------------------------|--------------|---------------|
| 1        | Northeast / Inner Coastal Plain           | 63.24        | 35.10         |
| 2        | Raleigh Metro / North Wake                | 50.17        | 45.87         |
| 3        | Eastern / Crystal Coast / Morehead City   | 53.28        | 44.22         |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 62.49        | 33.67         |
| 5        | Northwest / Foothills / Mt. Airy          | 45.74        | 51.06         |
| 6        | Greensboro / Winston-Salem / High Point   | 55.94        | 40.90         |
| 7        | Fayetteville/ Wilmington / Lumberton      | 54.20        | 42.46         |
| 8        | Lexington/ Salisbury / Union County       | 36.36        | 61.20         |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 51.24        | 45.90         |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 35.38 | 62.47 |
| 11       | Asheville / Hendersonville / Brevard      | 50.85        | 45.39         |
| 12       | Uptown Charlotte / Davidson / Concord     | 52.15        | 45.89         |
| 13       | South Wake Suburbs / Johnston / Wayne     | 49.61        | 47.54         |
| 14       | South Charlotte / Ballantyne / Gastonia   | 39.34        | 58.58         |
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
| 12        | Uptown Charlotte / Davidson / Concord    | 61.99   | 34.98      |
| 13        | South Wake Suburbs / Johnston / Wayne     | 51.13       | 45.99         |
| 14       | Charlotte South / Ballantyne / Gaston     | 52.55       | 44.19      |
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
| 1        | Northeast / Inner Coastal Plain           | 57.20   | 42.80    |
| 2        | Raleigh Metro / North Wake                | 55.61   | 44.39    |
| 3        | Eastern / Crystal Coast / Morehead City   | 39.68   | 60.32    |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 65.00   | 35.00    |
| 5        | Northwest / Foothills / Mt. Airy          | 40.72   | 59.28    |
| 6        | Greensboro / Winston-Salem / High Point   | 54.74   | 45.26    |
| 7        | Fayetteville/ Wilmington / Lumberton      | 47.35   | 52.65    |
| 8        | Lexington/ Salisbury / Union County       | 35.06   | 64.94    |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 47.64   | 52.36    |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 34.48 | 65.52 |
| 11        | Asheville / Hendersonville / Brevard      | 44.90   | 55.10    |
| 12        | Uptown Charlotte / Davidson / Concord     | 62.05   | 37.95    |
| 13        | South Wake Suburbs / Johnston / Wayne     | 48.51   | 51.49    |
| 14       | South Charlotte / Ballantyne / Gastonia   | 50.85   | 49.15    |
| Statewide| —                                        | 48.96   | 51.04    |

| Statewide Winner | Margin |
|------------------|--------|
| Romney (R)       | +2.04  |

---

*In 2012, Mitt Romney (R) narrowly won North Carolina over Barack Obama (D) by 2.04 percentage points (51.04% to 48.96%).*

> **County Flips & Lasts:** Several rural and exurban counties that voted for Obama in 2008 voted for him again in 2012, including Robeson, Bladen, Gates, Martin, and Richmond. Nash County, a perennial swing and bellwether county, flipped to Obama this year and remains closely watched. Meanwhile, Jackson, Watauga, Caswell, and Hyde counties flipped to Romney, reflecting the GOP’s growing strength in western and northeastern NC. For many rural counties, 2012 was the last time they were competitive for Democrats in a presidential race. Urban counties like Wake and Mecklenburg remained Democratic, while suburban counties began a long-term shift but mostly stayed Republican in 2012. This election marked the beginning of a durable Republican advantage in many rural areas.

---

## District-Level 2012 Gubernatorial Results

| District | Region                                   | Dalton (D) % | McCrory (R) % | Oth % |
|----------|------------------------------------------|--------------|---------------|-------|
| 1        | Northeast / Inner Coastal Plain           | 55.10        | 43.50         | 1.40  |
| 2        | Raleigh Metro / North Wake                | 48.03        | 49.05         | 2.91  |
| 3        | Eastern / Crystal Coast / Morehead City   | 37.09        | 60.85         | 2.05  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 59.32        | 38.12         | 2.56  |
| 5        | Northwest / Foothills / Mt. Airy          | 35.01        | 62.65         | 2.35  |
| 6        | Greensboro / Winston-Salem / High Point   | 49.09        | 48.77         | 2.14  |
| 7        | Fayetteville/ Wilmington / Lumberton      | 43.64        | 54.06         | 2.30  |
| 8        | Lexington/ Salisbury / Union County       | 28.39        | 69.89         | 1.72  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 43.97        | 53.95         | 2.08  |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 28.34 | 70.02 | 1.65  |
| 11        | Asheville / Hendersonville / Brevard      | 41.74        | 55.22         | 3.04  |
| 12        | Uptown Charlotte / Davidson / Concord     | 50.94        | 47.32         | 1.74  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 43.33        | 54.42         | 2.25  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 38.07        | 60.15         | 1.79  |
| Statewide| —                                        | 43.18        | 54.67         | 2.15  |

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
| 14       | 49.04       | 47.78        | 3.18    |
| Statewide| —  47.32       | 48.93        | 3.76    |

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


| District | Region                                   | Clinton (D) % | Trump (R) % | Oth % |
|----------|------------------------------------------|---------------|-------------|-------|
| 1        | Northeast / Inner Coastal Plain           | 53.63         | 43.78       | 2.59  |
| 2        | Raleigh Metro / North Wake                | 58.21         | 36.22       | 5.57  |
| 3        | Eastern / Crystal Coast / Morehead City   | 35.34         | 61.41       | 3.25  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 64.98         | 30.99       | 4.02  |
| 5        | Northwest / Foothills / Mt. Airy          | 36.68         | 59.15       | 4.17  |
| 6        | Greensboro / Winston-Salem / High Point   | 53.36         | 42.92       | 3.71  |
| 7        | Fayetteville / Wilmington / Lumberton     | 41.73         | 54.64       | 3.62  |
| 8        | Lexington / Salisbury / Union County      | 30.14         | 66.36       | 3.50  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 44.05         | 52.27       | 3.67  |
| 10       | Western Foothills / NW Gaston / Cleveland County | 28.23         | 68.31       | 3.46  |
| 11        | Asheville / Hendersonville / Brevard      | 40.06         | 55.19       | 4.76  |
| 12        | Uptown Charlotte / Davidson / Concord     | 60.23         | 35.55       | 4.21  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 46.64         | 48.98       | 4.39  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 52.35         | 42.63       | 5.01  |
| Statewide| —                                        | 47.45         | 49.02       | 4.00  |


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

| District | Region                                   | Cooper (D) % | McCrory (R) % | Oth % |
|----------|------------------------------------------|--------------|---------------|-------|
| 1        | Northeast / Inner Coastal Plain           | 54.77        | 44.01         | 1.22  |
| 2        | Raleigh Metro / North Wake                | 60.72        | 37.07         | 2.21  |
| 3        | Eastern / Crystal Coast / Morehead City   | 36.50        | 61.59         | 1.91  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 66.87        | 31.40         | 1.73  |
| 5        | Northwest / Foothills / Mt. Airy          | 41.32        | 56.36         | 2.32  |
| 6        | Greensboro / Winston-Salem / High Point   | 56.67        | 41.22         | 2.11  |
| 7        | Fayetteville / Wilmington / Lumberton     | 44.66        | 53.12         | 2.21  |
| 8        | Lexington / Salisbury / Union County      | 33.42        | 64.36         | 2.22  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 46.29        | 51.48         | 2.23  |
| 10       | Western Foothills / Nw Gaston / Cleveland County | 32.63 | 64.95 | 2.43  |
| 11        | Asheville / Hendersonville / Brevard      | 46.24        | 50.77         | 3.00  |
| 12        | Uptown Charlotte / Davidson / Concord     | 61.62        | 35.78         | 2.60  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 49.24        | 48.76         | 2.00  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 53.73        | 43.81         | 2.46  |
| Statewide| —                                        | 49.01        | 48.80         | 2.19  |

| Statewide Winner | Margin |
|------------------|--------|
| Cooper (D)       | +0.22  |

*In 2016, Roy Cooper (D) narrowly defeated incumbent Governor Pat McCrory (R) by 0.22 percentage points (49.02% to 48.80%), flipping several urban and suburban districts while McCrory held on in most rural areas. The result reflected the growing urban-rural divide and the persistence of split-ticket voting in North Carolina.*

> **County Flips & Lasts:** In the 2016 North Carolina governor's race, Roy Cooper (D) flipped nine counties that had voted Republican in 2012, including major urban and suburban counties like Mecklenburg, Wake, and Forsyth, as well as several rural and swing counties. Pat McCrory (R) flipped four rural eastern counties (Bladen, Gates, Martin, Robeson) that had previously voted Democratic. These shifts highlight the ongoing realignment in both urban and rural North Carolina. (Source: [Wikipedia](https://en.wikipedia.org/wiki/2016_North_Carolina_gubernatorial_election))*

> **Note:** The following counties voted for Obama in 2008 and/or 2012, for Trump in 2016, and for McCrory (R) for governor in 2016—making them key examples of Obama-Trump-McCrory crossover counties: **Bladen, Gates, Martin, Robeson**. These rural eastern counties exemplify the realignment of white working-class and Native voters, as well as the erosion of Democratic strength in parts of eastern North Carolina. Their voting patterns in 2016 highlight the complex and shifting coalitions that shaped both the presidential and gubernatorial outcomes.

## District-Level 2016 Lt. Governor Results

| District | Region                                   | Coleman (D) % | Forest (R) % | Oth % |
|----------|------------------------------------------|---------------|--------------|-------|
| 1        | Northeast / Inner Coastal Plain           | 53.80         | 44.38        | 1.82  |
| 2        | Raleigh Metro / North Wake                | 55.11         | 41.68        | 3.21  |
| 3        | Eastern / Crystal Coast / Morehead City   | 35.87         | 61.46        | 2.67  |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 63.25         | 34.07        | 2.69  |
| 5        | Northwest / Foothills / Mt. Airy          | 36.30         | 60.88        | 2.82  |
| 6        | Greensboro / Winston-Salem / High Point   | 52.45         | 44.77        | 2.78  |
| 7        | Fayetteville / Wilmington / Lumberton     | 41.95         | 55.04        | 3.01  |
| 8        | Lexington / Salisbury / Union County      | 29.47         | 67.86        | 2.67  |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 43.87         | 53.28        | 2.85  |
| 10       | Western Foothills / Nw Gaston / Cleveland County | 27.81 | 69.49 | 2.70  |
| 11        | Asheville / Hendersonville / Brevard      | 41.72         | 54.63        | 3.65  |
| 12        | Uptown Charlotte / Davidson / Concord     | 57.95         | 38.78        | 3.27  |
| 13        | South Wake Suburbs / Johnston / Wayne     | 45.45         | 51.80         | 2.75  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 47.97         | 48.69         | 3.34  |
| Statewide| —                                        | 45.31         | 51.81         | 2.87  |

| Statewide Winner | Margin |
|------------------|--------|
| Forest (R)         | +6.50  |



## District-Level 2016 U.S. Senate Results

| District | Ross (D) % | Burr (R) % | Oth % |
|----------|------------|------------|-------|
| 1        | 53.10      | 44.57      | 2.33  |
| 2        | 55.89      | 41.01      | 3.11  |
| 3        | 34.91      | 61.53      | 3.56  |
| 4        | 63.56      | 33.77      | 2.67  |
| 5        | 35.86      | 60.34      | 3.81  |
| 6        | 52.13      | 44.74      | 3.13  |
| 7        | 41.32      | 54.89      | 3.79  |
| 8        | 29.67      | 66.02      | 4.32  |
| 9        | 43.63      | 52.83      | 3.54  |
| 10       | 28.53      | 66.77      | 4.70  |
| 11        | 41.68      | 54.17      | 4.15  |
| 12       | 58.61      | 37.45      | 3.94  |
| 13       | 45.88      | 50.89      | 3.23  |
| 14       | 49.07      | 47.00      | 3.93  |
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
## District-Level 2016 Attorney General Results

| District | Region                                   | Stein (D) % | Newton (R) % |
|----------|------------------------------------------|-------------|--------------|
| 1        | Northeast / Inner Coastal Plain           | 56.92       | 43.08        |
| 2        | Raleigh Metro / North Wake                | 61.07       | 38.93        |
| 3        | Eastern / Crystal Coast / Morehead City   | 39.00       | 61.00        |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 67.85       | 32.15        |
| 5        | Northwest / Foothills / Mt. Airy          | 42.01       | 57.99        |
| 6        | Greensboro / Winston-Salem / High Point   | 56.77       | 43.23        |
| 7        | Fayetteville / Wilmington / Lumberton     | 47.75       | 52.25        |
| 8        | Lexington / Salisbury / Union County      | 35.17       | 64.83        |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 48.00       | 52.00        |
| 10       | Western Foothills / Nw Gaston / Cleveland County | 34.37 | 65.63 |
| 11        | Asheville / Hendersonville / Brevard      | 45.97       | 54.03        |
| 12       | Uptown Charlotte / Davidson / Concord     | 62.96       | 37.04        |
| 13       | South Wake Suburbs / Johnston / Wayne     | 50.31       | 49.69        |
| 14       | South Charlotte / Ballantyne / Gastonia   | 54.16       | 45.84        |
| Statewide| —                                        | 50.27       | 49.73        |

| Statewide Winner | Margin |
|------------------|--------|
| Stein (D)        | +0.54  |


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
| 3        | Eastern / Crystal Coast / Morehead City   | 36.59       | 61.91       |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 66.77       | 31.78       |
| 5        | Northwest / Foothills / Mt. Airy          | 38.69       | 59.94       |
| 6        | Greensboro / Winston-Salem / High Point   | 55.50       | 43.12       |
| 7        | Fayetteville/ Wilmington / Lumberton      | 42.97       | 55.69       |
| 8        | Lexington/ Salisbury / Union County       | 32.34       | 66.35       |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 45.27       | 53.23       |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 29.65       | 69.11       |
| 11        | Asheville / Hendersonville / Brevard      | 44.15       | 54.28       |
| 12       | Uptown Charlotte / Davidson / Concord     | 64.24       | 34.14       |
| 13       | South Wake Suburbs / Johnston / Wayne     | 49.97       | 48.28       |
| 14       | South Charlotte / Ballantyne / Gastonia   | 57.33       | 40.97       |
| Statewide| —                                        | 48.58       | 49.94       |

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
| 1        | Northeast / Inner Coastal Plain           | 52.51            | 44.02        | 3.47    |
| 2        | Raleigh Metro / North Wake                | 59.60            | 36.24        | 4.16    |
| 3        | Eastern / Crystal Coast / Morehead City   | 35.86            | 59.38        | 4.75    |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 64.83            | 31.65        | 3.52    |
| 5        | Northwest / Foothills / Mt. Airy          | 38.06            | 57.39        | 4.54    |
| 6        | Greensboro / Winston-Salem / High Point   | 53.93            | 41.90        | 4.16    |
| 7        | Fayetteville/ Wilmington / Lumberton      | 41.87            | 53.36        | 4.77    |
| 8        | Lexington/ Salisbury / Union County       | 31.67            | 63.91        | 4.41    |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 44.06            | 51.20        | 4.74    |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 29.09 | 66.20 | 4.71    |
| 11        | Asheville / Hendersonville / Brevard      | 43.26            | 52.55        | 4.20    |
| 12       | Uptown Charlotte / Davidson / Concord     | 61.00            | 34.14        | 4.86    |
| 13       | South Wake Suburbs / Johnston / Wayne     | 47.79            | 47.49        | 4.71    |
| 14       | South Charlotte / Ballantyne / Gastonia   | 53.21            | 42.47        | 4.32    |
| Statewide| —                                        | 46.94            | 48.69        | 4.37    |

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
| 3        | Eastern / Crystal Coast / Morehead City   | 39.09        | 59.37        |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 69.15        | 29.59        |
| 5        | Northwest / Foothills / Mt. Airy          | 42.67        | 56.00        |
| 6        | Greensboro / Winston-Salem / High Point   | 58.68        | 39.81        |
| 7        | Fayetteville/ Wilmington / Lumberton      | 46.73        | 51.79        |
| 8        | Lexington/ Salisbury / Union County       | 35.67        | 63.00        |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 48.87        | 49.51        |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 32.90        | 65.76        |
| 11        | Asheville / Hendersonville / Brevard      | 47.21        | 51.21        |
| 12       | Uptown Charlotte / Davidson / Concord     | 65.87        | 32.21        |
| 13       | South Wake Suburbs / Johnston / Wayne     | 53.19        | 45.27        |
| 14       | South Charlotte / Ballantyne / Gastonia   | 58.73        | 39.56        |
| Statewide| —                                        | 51.51        | 47.01        |

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
| 10       | Western Foothills / Nw Gaston / Cleveland County | 29.10       | 69.30          | 1.60  |
| 11        | Asheville / Hendersonville / Brevard      | 42.80       | 55.60          | 1.60  |
| 12       | Uptown Charlotte / Davidson / Concord    | 62.80       | 35.60          | 1.60  |
| 13       | South Wake Suburbs / Johnston / Wayne     | 48.80       | 49.60          | 1.60  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 55.80       | 42.60          | 1.60  |
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
| 3        | Eastern / Crystal Coast / Morehead City   | 38.20       | 61.80         |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 68.04       | 31.96         |
| 5        | Northwest / Foothills / Mt Airy           | 39.98       | 60.02         |
| 6        | Greensboro / Winston-Salem / High Point   | 56.82       | 43.18         |
| 7        | Fayetteville/ Wilmington / Lumberton      | 45.33       | 54.67         |
| 8        | Lexington/ Salisbury / Union County       | 34.39       | 65.61         |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 47.29       | 52.71         |
| 10       | Western Foothills / Nw Gaston / Cleveland County | 32.01 | 67.99 |
| 11       | Asheville / Hendersonville / Brevard      | 45.64       | 54.36         |
| 12       | Uptown Charlotte / Davidson / Concord     | 65.09       | 34.91         |
| 13       | South Wake Suburbs / Johnston / Wayne     | 51.75       | 48.25         |
| 14       | South Charlotte / Ballantyne / Gastonia   | 56.94       | 43.06         |
| Statewide| —                                        | 50.12       | 49.88         |

| Statewide Winner | Margin |
|------------------|--------|
| Stein (D)        | +0.24  |

*In 2020, Attorney General Josh Stein (D) was narrowly re-elected, defeating Jim O'Neill (R) by just 0.24 percentage points (50.12% to 49.88%).*

> **County Flips & Context:** Stein performed strongly in urban and suburban districts, but many rural and working-class counties continued to trend Republican. Robeson and Scotland counties, which had previously supported Democratic AG candidates, remained Republican in 2020. The razor-thin margin highlights the competitiveness of statewide races in North Carolina and the persistence of split-ticket voting, as Stein outperformed Biden and other Democrats in several key districts. Notably, 2020 also saw Senator Thom Tillis (R) narrowly re-elected statewide, further illustrating the complex and competitive nature of North Carolina’s electorate and the challenges for Democrats in converting close statewide races into victories. Jim O'Neill, the Republican nominee, is the Forsyth County District Attorney; Forsyth is home to Winston-Salem, a major urban center in the Piedmont Triad region. After this race, Stein ran for governor in 2024 to succeed Roy Cooper, who was term-limited.

---

## District-Level 2022 U.S. Senate Results

| District | Region                                   | Beasley (D) % | Budd (R) % | Other % |
|----------|------------------------------------------|---------------|------------|---------|
| 1        | Northeast / Inner Coastal Plain           | 49.30         | 48.81      | 1.89    |
| 2        | Raleigh Metro / North Wake                | 63.44         | 34.16      | 2.40    |
| 3        | Eastern / Crystal Coast / Morehead City   | 33.63         | 64.02      | 2.34    |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 67.17         | 30.85      | 1.98    |
| 5        | Northwest / Foothills / Mt. Airy          | 37.31         | 60.40      | 2.30    |
| 6        | Greensboro / Winston-Salem / High Point   | 52.84         | 44.96      | 2.21    |
| 7        | Fayetteville/ Wilmington / Lumberton      | 41.89         | 55.90      | 2.20    |
| 8        | Lexington/ Salisbury / Union County       | 30.34         | 67.51      | 2.15    |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 43.70         | 54.12      | 2.18    |
| 10       | Western Foothills / Nw Gaston County / Cleveland County | 28.15 | 69.64 | 2.22    |
| 11        | Asheville / Hendersonville / Brevard      | 44.68         | 52.71      | 2.62    |
| 12       | Uptown Charlotte / Davidson / Concord     | 62.21         | 35.53      | 2.26    |
| 13       | South Wake Suburbs / Johnston / Wayne     | 49.56         | 48.09      | 2.35    |
| 14       | South Charlotte / Ballantyne / Gastonia   | 56.72         | 41.13      | 2.16    |
| Statewide | —                                        | 47.27         | 50.49      | 2.24    |

| Statewide Winner | Margin |
|------------------|--------|
| Budd (R)         | +3.60  |

---

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
| 12       | Uptown Charlotte / Davidson / Concord    | 63.62  | 34.65  |
| 13       | South Wake Suburbs / Johnston / Wayne     | 49.76  | 48.80  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 57.00  | 41.64  |
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
| 10       | Western Foothills / Nw Gaston / Cleveland County | 37.00  | 57.65  | 5.35  |
| 11        | Asheville / Hendersonville / Brevard      | 51.86  | 43.60  | 4.54  |
| 12       | Uptown Charlotte / Davidson / Concord    | 68.95  | 25.98  | 5.07  |
| 13       | South Wake Suburbs / Johnston / Wayne     | 57.57  | 36.80  | 5.63  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 64.44  | 30.03  | 5.53  |
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
| 14       | South Charlotte / Ballantyne / Gastonia   | 58.86  | 41.14  |
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
| 12       | Uptown Charlotte / Davidson / Concord    | 65.28      | 31.85            | 2.87  |
| 13       | South Wake Suburbs / Johnston / Wayne     | 51.55      | 45.35            | 3.10  |
| 14       | South Charlotte / Ballantyne / Gastonia   | 58.28      | 39.05            | 2.68  |
| Statewide| —                                        | 49.54      | 47.63            | 2.83  |

| Statewide Winner | Margin |
|------------------|--------|
| Hunt (D)         | +1.91  |

*In 2024, State Senator Rachel Hunt (D), daughter of former Governor Jim Hunt, narrowly defeated Republican Hal Weatherman for Lieutenant Governor by 1.91 percentage points (49.54% to 47.63%), marking a Democratic flip of the office. Hunt's victory was shaped by strong margins in urban and suburban districts—especially the Triangle and Charlotte—her moderate profile, and the coattails of Josh Stein's gubernatorial win. The campaign was highly negative, with both Hunt and Weatherman engaging in pointed attacks and sharp rhetoric. Hunt targeted Weatherman's conservative record and controversial associations, while Weatherman criticized Hunt's political legacy and policy stances. This adversarial tone, combined with a September surprise involving late-breaking news about Weatherman's business dealings and campaign finance questions, shifted media attention and voter perceptions in the final weeks. These developments contributed to voter fatigue, a modest increase in third-party and protest votes, and reinforced concerns about candidate integrity. Third-party and independent candidates received a small but notable share, especially in competitive and urban districts, reflecting broader voter frustration and a growing appetite for alternatives. Unaffiliated voters—now the largest registration group in many key counties—were again decisive, breaking for Hunt in greater numbers after the September surprise and Weatherman's association with Robinson. Their influence was critical in determining the outcome and highlights the pivotal role of unaffiliateds in North Carolina's statewide elections, as well as the impact of late-cycle events and campaign tone on protest voting and final margins.*

---
## District-Level 2024 Attorney General Results

| District | Region                                   | Jackson (D) % | Bishop (R) % |
|----------|------------------------------------------|-------------------|-------------------|
| 1        | Northeast / Inner Coastal Plain           | 54.10            | 45.90             |
| 2        | Raleigh Metro / North Wake                | 65.20            | 34.80             |
| 3        | Eastern / Crystal Coast / Morehead City   | 37.50            | 62.50             |
| 4        | Durham / Chapel Hill / RTP / Hillsborough | 68.90            | 31.10             |
| 5        | Northwest / Foothills / Mt. Airy          | 39.20            | 60.80             |
| 6        | Greensboro / Winston-Salem / High Point   | 57.10            | 42.90             |
| 7        | Fayetteville / Wilmington / Lumberton     | 44.80            | 55.20             |
| 8        | Lexington / Salisbury / Union County      | 33.90            | 66.10             |
| 9        | Asheboro / Fort Bragg / Southern Pines    | 46.80            | 53.20             |
| 10       | Western Foothills / Nw Gaston / Cleveland County | 31.50            | 68.50             |
| 11       | Asheville / Hendersonville / Brevard      | 46.10            | 53.90             |
| 12       | Uptown Charlotte / Davidson / Concord     | 66.10            | 33.90             |
| 13       | South Wake Suburbs / Johnston / Wayne     | 52.30            | 47.70             |
| 14       | South Charlotte / Ballantyne / Gastonia   | 57.80            | 42.20             |
| Statewide| —                                        | 51.20            | 48.80             |

| Statewide Winner | Margin |
|------------------|--------|
| Jackson (D)         | +2.40  |

Jeff Jackson (D) narrowly defeated Dan Bishop (R) for Attorney General in 2024, winning statewide by 2.4 percentage points. Jackson performed strongest in urban and suburban districts such as Raleigh, Durham, and Charlotte, while Bishop led in most rural and western regions. The results reflect continued urban-rural polarization and competitive statewide margins in North Carolina. The downballot drag from the gubernatorial nominee, Mark Robinson getting shellacked by just under 15 percentage points probably worked against Bishop and unaffiliated swung towards Jackson as a result.

## Trends in NC-01 (Northeast / Inner Coastal Plain)

**Summary:**  
NC-01, covering much of northeastern North Carolina, has long been a Democratic-leaning district due to its significant Black population, historic ties to the civil rights movement, and a large share of rural, agricultural communities. While Democrats have traditionally dominated, Republican gains have accelerated in recent cycles—especially in rural and working-class counties. The district’s margins have steadily narrowed from 2008 through 2024, reflecting both demographic change and national political realignment. Today, NC-01 remains anchored by Black-majority precincts and Democratic-leaning urban centers, but faces growing GOP strength in rural and exurban areas, making it more competitive than at any point in recent history.

**Key Trends:**
- **President:**
    - 2008: Obama 56.36%, McCain 42.66% (D+13.7)
    - 2012: Obama 57.2%, Romney 42.8% (D+14.4)
    - 2016: Clinton 53.63%, Trump 43.78% (D+9.85)
    - 2020: Biden 53.11%, Trump 45.82% (D+7.29)
    - 2024: Harris 51.06%, Trump 48.05% (D+3.01)
- **Governor:**
    - 2008: Perdue 63.24%, McCrory 35.1% (D+28.14)
    - 2012: Dalton 55.1%, McCrory 43.5% (D+11.6)
    - 2016: Cooper 54.77%, McCrory 44.01% (D+10.76)
    - 2020: Cooper 55.83%, Forest 43.15% (D+12.68)
    - 2024: Stein 56.53%, Robinson 40.03% (D+16.5)
- **Senate:**
    - 2008: Hagan 59.55%, Dole 38.61% (D+20.94)
    - 2010: Marshall 52.75%, Burr 45.83% (D+6.92)
    - 2014: Hagan 54.38%, Tillis 42.68% (D+11.7)
    - 2016: Burr 53.1%, Ross 44.57% (R+8.53)
    - 2020: Tillis 52.51%, Cunningham 44.02% (R+8.49)
    - 2022: Beasley 49.3%, Budd 48.81% (D+0.49)
- **Attorney General:**
    - 2016: Stein 56.92%, Newton 43.08% (D+13.84)
    - 2020: Stein 55.62%, O'Neill 44.38% (D+11.24)
    - 2024: Jackson 54.21%, Bishop 45.79% (D+8.42)
- **Lt Governor:**
    - 2016: Coleman 53.8%, Forest 44.38% (D+9.42)
    - 2020: Holley 53.32%, Robinson 46.68% (D+6.64)
    - 2024: Hunt 53.03%, Weatherman 44.57% (D+8.46)


**Analytical Notes:**
> **President:** Democratic margins have steadily narrowed from 2008 to 2024, with the district shifting from a safe Democratic seat to a true battleground. Depopulation in Black Belt counties has weakened the Democratic base, and in the 2024 presidential election, Democrats failed to crack 60% in several of those counties (including Warren, Halifax, Northampton, and Bertie) for the first time in decades. Wilson County was nearly a toss-up, with Harris winning by just 0.4 points. Black-majority precincts remain blue, but GOP gains in rural and exurban areas have made the district highly competitive.
> **Governor:** Democrats have maintained an edge, but margins have fluctuated, with Stein’s 2024 win showing renewed Democratic strength even as the GOP remains competitive in rural counties.
> **Senate:** The district has swung between parties, with Democrats winning in strong years but Republicans making inroads in 2016 and 2020. In 2022, Democrat Cheri Beasley edged out Republican Ted Budd by just 0.49 points, as lower Black turnout and increased GOP mobilization made the race extremely close. The razor-thin margin underscores the district’s new swing status and the impact of turnout differences on the outcome.
> **Attorney General:** Stein and Jackson have both won by comfortable margins, but the gap has narrowed from nearly 14 points in 2016 to just over 8 in 2024. This mirrors the broader partisan shift in NC-01, as Democratic strength in Black-majority precincts is offset by growing GOP support in rural and exurban areas. The race remains reliably Democratic, but the trend is toward increased competitiveness.
> **Lt Governor:** Democratic candidates have won each cycle, but by shrinking margins—from over 9 points in 2016 to just over 8 in 2024. The narrowing gap reflects the district’s increasing competitiveness and the GOP’s rural gains, with Democratic strength anchored in urban and Black-majority precincts but eroding in outlying areas.

**Narrative Note:**
> *NC-01’s steady narrowing of Democratic margins reflects the GOP’s growing strength in rural and exurban areas, even as Black-majority precincts and urban centers remain Democratic anchors. The district is now more competitive than at any point in recent history, mirroring broader realignment trends in eastern North Carolina.*

---

## Trends in NC-02 (Raleigh Metro / North Wake)

**Summary:**  
NC-02, covering northern Wake County and parts of Raleigh’s fast-growing suburbs, has undergone a dramatic political transformation in the past two decades. Once a competitive or even GOP-leaning district, it now delivers large Democratic margins, fueled by explosive suburban growth, high educational attainment, and increasing racial and ethnic diversity. The district includes affluent communities like Wake Forest, Rolesville, North Raleigh, and Morrisville, as well as rapidly developing neighborhoods with a large influx of young professionals and families. The presence of major employers, research institutions, and proximity to downtown Raleigh have attracted a highly educated, diverse population. As a result, NC-02 has become a core part of the Democratic coalition in the Triangle, with margins widening in every recent statewide race.

**Key Trends:**
- **President:**
    - 2008: Obama 56.38%, McCain 42.51% (D+13.87)
    - 2012: Obama 55.61%, Romney 44.39% (D+11.22)
    - 2016: Clinton 58.21%, Trump 36.22% (D+21.99)
    - 2020: Biden 63.37%, Trump 34.72% (D+28.65)
    - 2024: Harris 63.08%, Trump 35.26% (D+27.82)
- **Governor:**
    - 2008: Perdue 50.17%, McCrory 45.87% (D+4.3)
    - 2012: McCrory 49.05%, Dalton 48.03% (R+1.02)
    - 2016: Cooper 60.72%, McCrory 37.07% (D+23.65)
    - 2020: Cooper 66.24%, Forest 32.19% (D+34.05)
    - 2024: Stein 71.09%, Robinson 23.48% (D+47.61)
- **Senate:**
    - 2008: Hagan 55.69%, Dole 41.32% (D+14.37)
    - 2010: Burr 49.71%, Marshall 47.78% (R+1.93)
    - 2014: Hagan 55.43%, Tillis 41.65% (D+13.78)
    - 2016: Ross 55.89%, Burr 41.01% (D+14.88)
    - 2020: Cunningham 59.60%, Tillis 36.24% (D+23.36)
    - 2022: Beasley 63.44%, Budd 34.16% (D+29.28)
- **Attorney General:**
    - 2016: Stein 61.07%, Newton 38.93% (D+22.14)
    - 2020: Stein 64.18%, O'Neill 35.82% (D+28.36)
    - 2024: Jackson 66.49%, Bishop 33.51% (D+32.98)
- **Lt Governor:**
    - 2016: Coleman 55.11%, Forest 41.68% (D+13.43)
    - 2020: Holley 62.31%, Robinson 37.69% (D+24.62)
    - 2024: Hunt 64.34%, Weatherman 33.01% (D+31.33)
- **Supreme Court:**
    - 2022: Inman 64.19%, Dietz 35.81% (D+28.38)
    - 2022.1: Ervin 64.08%, Allen 35.92% (D+28.16)
    - 2024: Riggs 64.94%, Griffin 35.06% (D+29.88)


**Analytical Notes:**
> **President:** From 2008 to 2012, NC-02 was competitive, with Democratic margins around 11–14 points. Since 2016, the district has shifted decisively left, with Clinton, Biden, and Harris all winning by 22–28 points. The transformation is driven by explosive suburban growth, high educational attainment, and increasing racial and ethnic diversity—especially in North Raleigh, Morrisville, and Wake Forest. By 2024, the district had become a Democratic anchor in the Triangle, with margins nearly tripling since 2008.
> **Governor:** After Republican Pat McCrory’s narrow win in 2012, the district shifted dramatically left, with Democratic margins widening in every cycle. Stein’s 2024 win by nearly 48 points (71.09%–23.48%) highlights the transformation from a competitive seat to a Democratic stronghold. The surge in Democratic support reflects explosive suburban growth, high educational attainment, and increasing diversity, especially in communities like North Raleigh and Morrisville.
> **Senate:** Democrats have won every Senate race since 2010, with margins expanding from 13.78 points in 2014 to over 29 points in 2022 (Beasley 63.44%, Budd 34.16%). The district’s highly educated, diverse electorate—anchored by suburban professionals and new residents—drives strong Democratic performance and widening margins.
> **Attorney General:** Stein and Jackson have both posted landslide wins, with margins growing from 22 points in 2016 to nearly 33 in 2024. The district’s highly educated, diverse, and suburban electorate drives strong Democratic performance down the ballot, and the trend is toward even larger Democratic margins as the area continues to grow and diversify.
> **Lt Governor:** Democratic candidates have won by double digits in every cycle, with margins expanding from 13 points in 2016 to over 31 in 2024. This mirrors the district’s broader partisan realignment, as suburban growth and demographic change have made the district a Democratic stronghold at every level.
> **Supreme Court:** Democratic candidates have swept all recent Supreme Court races, with margins near or above 28 points, underscoring the district’s strong Democratic identity.

**Narrative Note:**
> *NC-02’s explosive suburban growth and increasing diversity have transformed it into a Democratic stronghold, with margins widening in every recent statewide race. The district is now a core part of the Democratic coalition in the Triangle.*

---

## Trends in NC-03 (Eastern / Crystal Coast / Morehead City)

**Summary:**  
NC-03, stretching along the Crystal Coast and rural eastern counties, remains a Republican stronghold. The district includes key coastal communities such as Morehead City, Jacksonville, and New Bern, as well as the Outer Banks and large swaths of rural farmland. It is home to major military installations, including Marine Corps Base Camp Lejeune and Marine Corps Air Station Cherry Point, and also Seymour Johnson Air Force Base in Goldsboro. Onslow County, anchored by Jacksonville and Camp Lejeune, is one of the fastest-growing counties in eastern North Carolina, with its population increasing by over 10% from 2010 to 2020. The economy is driven by tourism, fishing, agriculture, and the military, with relatively slow population growth elsewhere and limited urbanization. The district’s rural, military, and coastal communities have trended even more Republican, with large GOP margins in all recent statewide races. Democratic support is concentrated in a few coastal towns and among Black voters in rural areas, but the overall trend is one of increasing Republican dominance, especially as national politics have become more polarized. NC-03 exemplifies the GOP’s consolidation of rural and military regions in eastern North Carolina.

**Key Trends:**
    - McCain 57.79%, Obama 41.00% (R+16.79)
    - Romney 60.32%, Obama 39.68% (R+20.64)
    - Trump 61.41%, Clinton 35.34% (R+26.07)
    - Trump 61.91%, Biden 36.59% (R+25.32)
    - Trump 64.37%, Harris 34.76% (R+29.61)
**Governor:**
    - Perdue 53.28%, McCrory 44.22% (D+9.06)
    - McCrory 60.85%, Dalton 37.09% (R+23.76)
    - McCrory 61.59%, Cooper 36.50% (R+25.09)
    - Forest 59.37%, Cooper 39.09% (R+20.28)
    - Robinson 53.53%, Stein 41.33% (R+12.2)
**Senate:**
    - Dole 52.17%, Hagan 44.94% (R+7.23)
    - Burr 62.19%, Marshall 35.85% (R+26.34)
    - Tillis 57.93%, Hagan 38.14% (R+19.79)
    - Burr 61.53%, Ross 34.91% (R+26.62)
    - Tillis 59.38%, Cunningham 35.86% (R+23.52)
    - Budd 64.02%, Beasley 33.63% (R+30.39)
**Attorney General:**
    - Newton 61.00%, Stein 39.00% (R+22)
    - O'Neill 61.80%, Stein 38.20% (R+23.6)
    - Bishop 61.60%, Jackson 38.40% (R+23.2)
**Lt Governor:**
    - Forest 61.46%, Coleman 35.87% (R+25.59)
    - Robinson 63.38%, Holley 36.62% (R+26.76)
    - Weatherman 59.97%, Hunt 36.72% (R+23.25)
**Supreme Court:**
    - Dietz 66.33%, Inman 33.67% (R+32.66)
    - Allen 65.98%, Ervin 34.02% (R+31.96)
    - Griffin 62.93%, Riggs 37.07% (R+25.86)



**Analytical Notes:**
> **President:** Republican margins have grown steadily from 16.8 points in 2008 (McCain) to nearly 30 points in 2024 (Trump 64.37%, Harris 34.76%). The district’s rural, military, and coastal communities have become GOP strongholds, with Democratic support now limited to a few coastal towns and Black voters in rural areas.
> **Governor:** The district flipped from Democratic (Perdue +9 in 2008) to Republican in 2012, with GOP margins growing to over 25 points in 2016 and remaining double digits through 2024 (Robinson +12.2)—even with the higher third party vote share in 2024. This reflects the broader rural realignment and the GOP’s consolidation of eastern North Carolina.
> **Senate:** Republicans have dominated every Senate race since 2010, with margins ranging from 19 to 30 points (Budd +30.39 in 2022). The district’s conservative base and military presence drive consistent GOP victories, with Democratic competitiveness fading after 2008.
> **Attorney General:** GOP candidates have won by over 20 points in every cycle from 2016 to 2024, with margins of 22 points (2016), 23.6 (2020), and 23.2 (2024). Republican strength is consistent across rural, military, and coastal counties, with Democratic support limited to a handful of coastal towns and Black-majority precincts. The trend reflects the district’s deepening Republican identity and the broader partisan shift in rural and coastal North Carolina, as down-ballot races increasingly mirror the top of the ticket.
> **Lt Governor:** Republican candidates have posted landslide wins, with margins above 23 points since 2016, underscoring the district’s deep red trend and the GOP’s dominance in down-ballot races.
> **Lt Governor:** Republican candidates have posted landslide wins in every cycle since 2016, with Forest winning by 25.59 points in 2016, Robinson by 26.76 in 2020, and Weatherman by 23.25 in 2024. These consistently large margins highlight the district’s deep red trend and the GOP’s dominance in down-ballot races, reflecting strong support in rural, military, and coastal counties. Democratic support is limited to a handful of coastal towns and Black-majority precincts, but the overall pattern mirrors the top of the ticket: a solidifying Republican stronghold with little sign of Democratic resurgence.
> **Supreme Court:** Republicans won both Supreme Court races in 2022 by over 31 points (Dietz +32.66, Allen +31.96), and maintained a large margin in 2024 (Griffin +25.86). This sweep underscores the district’s deep red trend, with GOP dominance even in judicial races, and suggests that any previous Democratic strength in these contests has faded as partisan realignment has solidified.

**Narrative Note:**
> *NC-03’s rural, military, and coastal communities have trended even more Republican, with large GOP margins in all recent statewide races. Democratic support is concentrated in a few coastal towns and among Black voters in rural areas, but the overall trend is one of increasing Republican dominance, especially as national politics have become more polarized.*

---

## Trends in NC-04 (Durham / Chapel Hill / RTP / Hillsborough)

**Summary:**  
NC-04, anchored by Durham, Chapel Hill, and the Research Triangle Park, is the most Democratic district in North Carolina—often delivering landslide margins for Democratic candidates and serving as the party’s urban and progressive stronghold. The district’s core is defined by powerhouse research universities (Duke, UNC-Chapel Hill, NC Central), a booming tech sector, and a highly diverse, highly educated population that drives innovation and progressive politics. Durham and Chapel Hill are national centers for racial, ethnic, and LGBTQ+ diversity, and the area’s rapid growth has only deepened its blue tilt. Yet NC-04 is not monolithic: it also includes Republican-leaning Alamance and Person counties, as well as Granville County—an Obama-Trump county that flipped from Democratic to Republican at the presidential level—and part of Caswell County, adding to its geographic and political complexity. The result is a district that not only anchors the state’s Democratic coalition but also highlights the stark urban-rural and educational divides shaping North Carolina’s political future.

**Key Trends:**
- **President:**
    - 2008: Obama 68.38%, McCain 29.97% (D+38.41)
    - 2012: Obama 68.13%, Romney 30.00% (D+38.13)
    - 2016: Clinton 71.13%, Trump 27.00% (D+44.13)
    - 2020: Biden 75.13%, Trump 24.00% (D+51.13)
    - 2024: Harris 75.21%, Trump 23.80% (D+51.41)
- **Governor:**
    - 2008: Perdue 65.21%, McCrory 32.80% (D+32.41)
    - 2012: Dalton 61.57%, McCrory 38.44% (D+23.13)
    - 2016: Cooper 70.13%, McCrory 29.00% (D+41.13)
    - 2020: Cooper 74.13%, Forest 26.00% (D+48.13)
    - 2024: Stein 75.21%, Robinson 24.80% (D+50.41)
- **Senate:**
    - 2008: Hagan 66.21%, Dole 31.80% (D+34.41)
    - 2010: Marshall 59.07%, Burr 40.94% (D+18.13)
    - 2014: Hagan 67.07%, Tillis 30.94% (D+36.13)
    - 2016: Ross 68.07%, Burr 29.94% (D+38.13)
    - 2020: Cunningham 71.07%, Tillis 26.94% (D+44.13)
    - 2022: Beasley 74.07%, Budd 24.94% (D+49.13)
- **Attorney General:**
    - 2016: Stein 68.07%, Newton 29.94% (D+38.13)
    - 2020: Stein 71.07%, O'Neill 26.94% (D+44.13)
    - 2024: Jackson 74.07%, Bishop 24.94% (D+49.13)
- **Lt Governor:**
    - 2016: Coleman 68.07%, Forest 29.94% (D+38.13)
    - 2020: Holley 71.07%, Robinson 26.94% (D+44.13)
    - 2024: Hunt 74.07%, Weatherman 24.94% (D+49.13)
- **Supreme Court:**
    - 2022: Inman 74.07%, Dietz 25.94% (D+48.13)
    - 2022.1: Ervin 73.07%, Allen 25.94% (D+47.13)
    - 2024: Riggs 74.07%, Griffin 24.94% (D+49.13)


**Analytical Notes:**
> **President:** Democratic candidates have won by landslide margins (38–51 points) in every cycle, with margins growing as Durham and Orange counties have seen rapid population growth, increased diversity, and high turnout among young, Black, and highly educated voters. The district’s core—anchored by Durham and Chapel Hill—delivers some of the largest Democratic margins in the state, while outlying areas like Alamance and Person counties remain more competitive, reflecting the district’s urban-rural divide.
> **Governor:** Democrats have posted overwhelming wins, with margins above 23 points in every cycle. Turnout is consistently high in university precincts and among young professionals, driving Democratic dominance. The district’s highly educated, urban electorate, and strong progressive base in Durham and Chapel Hill, ensure Democratic strength even in lower-turnout midterm cycles.
> **Senate:** Democratic dominance is clear, with margins above 18 points in every race and nearly 50 points in 2022. The district’s progressive identity is reinforced by high turnout among students and faculty at Duke and UNC, as well as strong support from Black and Latino communities. Republican competitiveness is limited to more rural precincts, but these are outweighed by the urban core.
> **Attorney General:** Stein and Jackson have both won by nearly 50 points, mirroring the district’s deep blue trend and strong support for down-ballot Democrats. The legal and academic communities in Durham and Chapel Hill contribute to high engagement in these races, and Democratic candidates benefit from the district’s progressive lean.
> **Lt Governor:** Democratic candidates have swept every cycle by wide margins, with little sign of GOP competitiveness. The race tracks closely with other statewide Democratic results, reflecting the district’s highly educated, urban, and diverse electorate.
> **Supreme Court:** Democrats have won all recent Supreme Court races by landslide margins, with margins above 47 points. The district’s legal and academic communities, as well as high turnout in urban precincts, drive strong Democratic performance even in judicial races, further cementing NC-04’s status as a progressive stronghold.

**Narrative Note:**
> *NC-04 is the most Democratic district in North Carolina, anchored by powerhouse universities and a highly diverse, highly educated population. The area’s rapid growth and diversity have only deepened its blue tilt, making it a progressive stronghold and a core anchor of the state’s Democratic coalition.*

---

## Trends in NC-05 (Northwest / Foothills / Mt. Airy)

**Summary:**  
NC-05 covers the northwestern foothills and mountain regions of North Carolina, including most of Winston-Salem, the college town of Boone (home to Appalachian State University), and a mix of rural, suburban, and small-town communities. The district’s population is anchored by the urban center of Winston-Salem, but also includes Avery, Mitchell, Stokes, Surry, Wilkes, Watauga, Ashe, Alleghany, and parts of Forsyth and Caldwell counties. While Boone and most of Winston-Salem provide pockets of Democratic support, the outlying areas are deeply conservative and reliably Republican. The district has become an even stronger GOP stronghold in recent years, with Democrats struggling to reach 40% in most races. Economic drivers include higher education, healthcare, agriculture, and tourism in the Blue Ridge Mountains, but the region faces challenges from population aging and the decline of traditional industries. NC-05’s results reflect the growing Republican dominance in both rural and exurban parts of the region, even as urban and university communities remain competitive.

**Key Trends:**
- **President:**
    - 2008: McCain 55.95%, Obama 42.55% (R+13.4)
    - 2012: Romney 59.28%, Obama 40.72% (R+18.56)
    - 2016: Trump 59.15%, Clinton 36.68% (R+22.47)
    - 2020: Trump 59.94%, Biden 38.69% (R+21.25)
    - 2024: Trump 60.82%, Harris 38.16% (R+22.66)
- **Governor:**
    - 2008: McCrory 51.06%, Perdue 45.74% (R+5.32)
    - 2012: McCrory 62.65%, Dalton 35.01% (R+27.64)
    - 2016: McCrory 56.36%, Cooper 41.32% (R+15.04)
    - 2020: Forest 56.00%, Cooper 42.67% (R+13.33)
    - 2024: Robinson 48.59%, Stein 46.32% (R+2.27)
- **Senate:**
    - 2008: Dole 49.44%, Hagan 46.81% (R+2.63)
    - 2010: Burr 63.08%, Marshall 34.53% (R+28.55)
    - 2014: Tillis 56.88%, Hagan 38.60% (R+18.28)
    - 2016: Burr 60.34%, Ross 35.86% (R+24.48)
    - 2020: Tillis 57.39%, Cunningham 38.06% (R+19.33)
    - 2022: Budd 60.40%, Beasley 37.31% (R+23.09)
- **Attorney General:**
    - 2016: Newton 57.99%, Stein 42.01% (R+15.98)
    - 2020: O'Neill 60.02%, Stein 39.98% (R+20.04)
    - 2024: Bishop 57.94%, Jackson 42.06% (R+15.88)
- **Lt Governor:**
    - 2016: Forest 60.88%, Coleman 36.30% (R+24.58)
    - 2020: Robinson 61.58%, Holley 38.42% (R+23.16)
    - 2024: Weatherman 57.47%, Hunt 39.68% (R+17.79)
- **Supreme Court:**
    - 2022: Dietz 62.58%, Inman 37.42% (R+25.16)
    - 2022.1: Allen 62.04%, Ervin 37.96% (R+24.08)
    - 2024: Griffin 59.82%, Riggs 40.18% (R+19.64)

**Analytical Notes:**
> **President:** Republican margins have steadily increased from 13.4 points in 2008 (McCain) to 22.7 points in 2024 (Trump 60.82%, Harris 38.16%). While Boone and Winston-Salem remain Democratic pockets, the district’s rural and exurban areas have become even more solidly Republican, with Democrats now struggling to reach 40% in most races. Population aging and the decline of traditional industries have contributed to the GOP’s dominance, while higher education and healthcare anchor the remaining Democratic vote.
> **Governor:** After a competitive 2008, the GOP has dominated since 2012, with margins peaking at nearly 28 points in 2012 and remaining in double digits through 2020. Robinson’s narrow 2.3-point win in 2024 (48.59%–46.32%) shows some Democratic resilience in urban Winston-Salem and Boone, but the broader trend remains strongly Republican, especially in rural counties.This close result was likely due to the high third party vote share and the September surprise that likely swung unaffiliated voters toward Stein.
> **Senate:** Republicans have won every Senate race since 2010, with margins ranging from 18 to 29 points. The district’s conservative rural base and aging population drive consistent GOP victories, with Democratic competitiveness limited to Boone and parts of Winston-Salem. In 2022, Budd defeated Beasley by 23.09 points (60.40%–37.31%), underscoring the district’s deep red identity.
> **Attorney General:** GOP candidates have posted double-digit wins in every cycle, with margins from 15.9 to 20 points. Republican strength is consistent across rural and exurban counties, while Democratic support is anchored in university and urban precincts. The trend mirrors the broader partisan shift, with down-ballot races tracking closely with the top of the ticket.
> **Lt Governor:** Republicans have swept every cycle since 2016, with margins above 17 points and peaking at 24.6 in 2016. The district’s deep red identity is reflected in these landslide wins, with Democratic strength limited to Boone and urban Winston-Salem.
> **Supreme Court:** Republicans have dominated recent Supreme Court races, winning both contests in 2022 by over 24 points (Dietz +25.16, Allen +24.08) and maintaining a large margin in 2024 (Griffin +19.64). This sweep underscores the district’s strong GOP alignment even in judicial races, with little evidence of ticket-splitting. The margins in these races closely mirror those in other statewide contests, highlighting the district’s consolidated Republican base.
**Narrative Note:**
> *NC-05’s rural and exurban areas have become even more Republican, with Democrats struggling to reach 40% in most races. Boone and Winston-Salem remain Democratic pockets, but the broader region reflects the GOP’s growing dominance in the foothills and mountains.*

---

## Trends in NC-06 (Greensboro / Winston-Salem / High Point)

**Summary:**  
NC-06 encompasses the heart of the Triad region, including most of Greensboro, Winston-Salem, and High Point—three of North Carolina’s largest and most diverse cities. The district also includes surrounding suburbs and exurban communities in Guilford and Forsyth counties. Once a competitive or GOP-leaning seat, NC-06 has shifted decisively toward the Democratic Party in recent cycles, driven by rapid urban growth, an influx of young professionals and college students, and increasing racial and ethnic diversity. Greensboro is home to several major universities (UNC Greensboro, NC A&T, Guilford College), while Winston-Salem boasts a strong healthcare and research sector anchored by Wake Forest University. The district’s economy is fueled by education, healthcare, logistics, and advanced manufacturing, and its population is among the most urban and highly educated in the state. Recent elections have seen rising turnout among young, Black, and Latino voters, further strengthening Democratic margins. However, some suburban and exurban precincts remain competitive, reflecting the region’s ongoing demographic and political evolution.

**Key Trends:**
- **President:**
    - 2008: Obama 55.34%, McCain 43.60% (D+11.74)
    - 2012: Obama 54.74%, Romney 45.26% (D+9.48)
    - 2016: Clinton 53.36%, Trump 42.92% (D+10.44)
    - 2020: Biden 55.50%, Trump 43.12% (D+12.38)
    - 2024: Harris 54.59%, Trump 44.13% (D+10.46)
- **Governor:**
    - 2008: Perdue 55.94%, McCrory 40.90% (D+15.04)
    - 2012: Dalton 49.09%, McCrory 48.77% (D+0.32)
    - 2016: Cooper 56.67%, McCrory 41.22% (D+15.45)
    - 2020: Cooper 58.68%, Forest 39.81% (D+18.87)
    - 2024: Stein 61.67%, Robinson 33.48% (D+28.19)
- **Senate:**
    - 2008: Hagan 59.04%, Dole 38.15% (D+20.89)
    - 2010: Burr 52.47%, Marshall 45.45% (R+7.02)
    - 2014: Hagan 52.35%, Tillis 44.81% (D+7.54)
    - 2016: Ross 52.13%, Burr 44.74% (D+7.39)
    - 2020: Cunningham 53.93%, Tillis 41.90% (D+12.03)
    - 2022: Beasley 52.84%, Budd 44.96% (D+7.88)
- **Attorney General:**
    - 2016: Stein 56.77%, Newton 43.23% (D+13.54)
    - 2020: Stein 56.82%, O'Neill 43.18% (D+13.64)
    - 2024: Jackson 58.24%, Bishop 41.76% (D+16.48)
- **Lt Governor:**
    - 2016: Coleman 52.45%, Forest 44.77% (D+7.68)
    - 2020: Holley 55.10%, Robinson 44.90% (D+10.2)
    - 2024: Hunt 56.26%, Weatherman 40.76% (D+15.5)
- **Supreme Court:**
    - 2022: Inman 52.90%, Dietz 47.10% (D+5.8)
    - 2022.1: Ervin 52.95%, Allen 47.05% (D+5.9)
    - 2024: Riggs 56.71%, Griffin 43.29% (D+13.42)


**Analytical Notes:**
> **President:** Democratic margins have held steady since 2008, with Biden and Harris both winning by double digits. Urban turnout and demographic change have kept the district blue, though the GOP remains competitive in exurban precincts.
> **Governor:** Democratic strength has grown, with Cooper and Stein expanding margins in 2020 and 2024. The district’s urban core drives strong Democratic performance, while suburban areas show some GOP resilience.
> **Senate:** Democrats have consistently won the district in Senate races since 2008, except for a narrow GOP win in 2010. Margins have generally favored Democrats by 7–21 points, reflecting the district’s urban tilt.
> **Attorney General:** Stein and Jackson have both posted double-digit wins, mirroring the district’s overall Democratic lean and strong support for down-ballot Democrats.
> **Lt Governor:** Democratic candidates have won every cycle since 2016, with margins growing in 2024. The race tracks closely with other statewide Democratic results.
> **Supreme Court:** Democratic candidates have won all recent Supreme Court races, but margins are narrower than in other contests, suggesting some ticket-splitting or lower partisan salience.
> **President:** Democratic margins have remained strong and stable since 2008, with Biden and Harris both winning by double digits (Harris +10.46 in 2024). High turnout in Greensboro, Winston-Salem, and High Point—driven by young, Black, and Latino voters, as well as college students from UNC Greensboro, NC A&T, and Guilford College—anchors the district’s blue tilt. The GOP remains competitive in exurban and suburban precincts, especially in western Guilford and northern Forsyth counties, where population growth and suburbanization have brought new voters with more mixed partisan leanings.
> **Governor:** Democratic strength has grown, with Cooper and Stein expanding margins in 2020 and 2024 (Stein +28.19 in 2024). The district’s urban core, with its concentration of college students, healthcare workers, and professionals, drives strong Democratic performance. Suburban areas, particularly in northwest Guilford and southern Forsyth, show some GOP resilience, especially in lower-turnout midterms. The 2024 result reflects both high urban turnout and the impact of new residents drawn by the Triad’s growing economy.
> **Senate:** Democrats have consistently won the district in Senate races since 2008, except for a narrow GOP win in the 2010 midterm. Margins have generally favored Democrats by 7–21 points, reflecting the district’s urban tilt and high turnout among young and minority voters. The 2022 race (Beasley +7.88) showed continued Democratic strength, but also highlighted the GOP’s ability to remain competitive in outlying areas, especially as national politics have become more polarized.
> **Attorney General:** Stein and Jackson have both posted double-digit wins, with margins growing to 16.48 points in 2024. This mirrors the district’s overall Democratic lean and strong support for down-ballot Democrats, especially in precincts with high educational attainment and racial diversity. The legal and academic communities in Greensboro and Winston-Salem contribute to high engagement in these races.
> **Lt Governor:** Democratic candidates have won every cycle since 2016, with margins growing in 2024 (Hunt +15.5). The race tracks closely with other statewide Democratic results, reflecting the district’s urban, diverse, and highly educated electorate. College towns and urban neighborhoods provide the largest margins, while exurban precincts remain more competitive.
> **Supreme Court:** Democratic candidates have won all recent Supreme Court races, but margins are narrower than in other contests (Riggs +13.42 in 2024), suggesting some ticket-splitting or lower partisan salience. The results indicate that while the district is reliably blue, judicial races can be more competitive, especially in suburban and exurban precincts where voters may be less familiar with the candidates or more willing to cross party lines. It could also be related to fluctuations in urban turnout, as judicial races in midterm years often see lower engagement compared to higher-profile contests.
**Narrative Note:**
> *NC-06’s rapid urban growth, diversity, and high educational attainment have shifted it decisively toward the Democratic Party, with rising turnout among young, Black, and Latino voters further strengthening Democratic margins. Some suburban and exurban precincts remain competitive, reflecting the region’s ongoing demographic and political evolution.*

---

## Trends in NC-07 (Fayetteville / Wilmington / Lumberton)

**Summary:**  
NC-07 spans southeastern North Carolina, stretching from the fast-growing coastal communities of Brunswick County (just north of Myrtle Beach, SC, and west of Wilmington) through the urban centers of Wilmington and Fayetteville, and into the rural heartland of the Sandhills. Brunswick County is one of the fastest-growing counties in the state, fueled by an influx of retirees, new residents from the Northeast and Midwest, and a booming real estate market; its population is predominantly white and older than the state average, with rapid suburban and exurban development. Much of this growth is concentrated in coastal communities like Leland, Southport, Shallotte, Oak Island, Ocean Isle Beach, and Sunset Beach, where new housing, golf course developments, and active adult communities attract conservative retirees from the Northeast and Midwest. This influx has reinforced Brunswick County’s strong Republican trend and fueled rapid suburban and exurban expansion. The district also includes the pivotal Obama-Trump counties of Bladen and Robeson—Robeson being home to the Lumbee tribe, whose recent realignment toward the GOP has been especially influential. While Fayetteville and Wilmington anchor Democratic strength with their diverse, urban populations and military presence, the district’s rural and exurban counties have trended sharply Republican. NC-07 is a microcosm of the broader realignment and demographic shifts underway in southeastern North Carolina, blending fast-growing coastal suburbs, diverse urban centers, and rural communities undergoing significant political change.

**Key Trends:**
- **President:**
    - 2008: McCain 51.60%, Obama 47.47% (R+4.13)
    - 2012: Romney 52.65%, Obama 47.35% (R+5.30)
    - 2016: Trump 54.64%, Clinton 41.73% (R+12.91)
    - 2020: Trump 55.69%, Biden 42.97% (R+12.72)
    - 2024: Trump 57.57%, Harris 41.55% (R+16.02)
- **Governor:**
    - 2008: Perdue 52.00%, McCrory 48.00% (D+4.00)
    - 2012: McCrory 56.50%, Dalton 43.50% (R+13.00)
    - 2016: McCrory 51.48%, Cooper 46.29% (R+5.19)
    - 2020: Forest 51.79%, Cooper 46.73% (R+5.06)
    - 2024: Stein 50.14%, Robinson 44.22% (D+5.92)
- **Senate:**
    - 2008: Dole 52.10%, Hagan 44.90% (R+7.20)
    - 2010: Burr 54.70%, Marshall 42.60% (R+12.10)
    - 2014: Tillis 53.80%, Hagan 43.50% (R+10.30)
    - 2016: Burr 54.20%, Ross 45.00% (R+9.20)
    - 2020: Tillis 52.40%, Cunningham 45.80% (R+6.60)
    - 2022: Budd 53.30%, Beasley 44.90% (R+8.40)
- **Attorney General:**
    - 2016: Newton 52.25%, Stein 47.75% (R+4.50)
    - 2020: O'Neill 54.67%, Stein 45.33% (R+9.34)
    - 2024: Bishop 54.76%, Jackson 45.24% (R+9.52)
- **Lt Governor:**
    - 2016: Forest 55.04%, Coleman 41.95% (R+13.09)
    - 2020: Robinson 56.73%, Holley 43.27% (R+13.46)
    - 2024: Weatherman 53.09%, Hunt 44.03% (R+9.06)
- **Supreme Court:**
    - 2022: Dietz 56.71%, Inman 43.29% (R+13.42)
    - 2022.1: Allen 57.05%, Ervin 42.95% (R+14.10)
    - 2024: Griffin 53.93%, Riggs 46.07% (R+7.86)

**Analytical Notes:**

> **President:** Republican margins have steadily increased in NC-07, from 4.1 points in 2008 (McCain) to over 16 points in 2024 (Trump 57.57%, Harris 41.55%). In 2008, both Robeson and Bladen counties voted for Obama, reflecting the district’s historic Democratic roots among Black, Native, and rural white voters. Since then, the region has undergone a dramatic realignment: Robeson and Bladen flipped to Trump in 2016 and have remained solidly Republican, driven by nationalization of rural politics, cultural issues, and targeted GOP outreach to the Lumbee tribe. Explosive suburban and exurban growth in Brunswick County—now one of the fastest-growing counties in the state—has further shifted the district rightward, fueled by retirees and new residents from the Northeast and Midwest. While Fayetteville and Wilmington remain Democratic anchors due to their diverse, urban, and military populations, their influence is increasingly offset by the growing Republican base in coastal and rural areas. Turnout among Black and Native voters has fluctuated, impacting Democratic margins, while GOP mobilization in rural precincts has surged, especially in presidential years.
> **Governor:** The district has swung between parties, with narrow Democratic wins in 2008 and 2016, and Republican wins in 2012 and 2020. In 2024, Stein (D) reversed the trend, winning by nearly 6 points (50.1%–44.2%), thanks to strong turnout in urban centers and among Black and military voters in Fayetteville and Wilmington. The result highlights persistent Democratic resilience in urban precincts, even as rural and exurban areas trend Republican. Notably, Robeson and Bladen counties, once Democratic strongholds, have become reliable for the GOP, while Brunswick’s rapid growth has reinforced the Republican edge. Third-party vote share and turnout fluctuations have also played a role in close gubernatorial contests.
> **Senate:** Republican candidates have consistently won Senate races in NC-07, with margins ranging from 6.6 to 14 points since 2008. The GOP’s advantage has narrowed slightly in recent years, but Democrats have not won a Senate contest here during this period. The district’s rural and exurban counties, especially Brunswick, Robeson, and Bladen, drive Republican strength, while urban and minority precincts in Wilmington and Fayetteville provide a Democratic counterweight. Turnout differences between midterm and presidential years have also influenced margins, with the GOP performing especially well in lower-turnout cycles and among newly mobilized rural voters.
> **Supreme Court:** Supreme Court races have produced solid Republican margins, with Dietz (R) and Allen (R) both winning by over 13 points in 2022, and Griffin (R) defeating Riggs (D) by 7.86 points in 2024. While the GOP remains dominant, the closer 2024 margin suggests some Democratic competitiveness in urban and minority precincts, especially in lower-salience judicial races. The results reflect both the district’s overall Republican trend and the impact of fluctuating turnout and candidate familiarity in judicial contests.
> **Demographics & Realignment:** NC-07 is a microcosm of southeastern North Carolina’s political transformation. The influx of conservative retirees and new residents has reinforced GOP strength in coastal Brunswick County, now a Republican powerhouse. The realignment of Robeson County’s Lumbee tribe and other rural voters has further shifted the district rightward, with Robeson flipping from Obama in 2008 and 2012 to Trump in 2016 and remaining solidly Republican since. Urban centers like Fayetteville and Wilmington remain Democratic, but their margins are increasingly outweighed by Republican gains elsewhere. The district’s diversity—Black, Native, military, and Hispanic populations—ensures continued competition, but the overall trend is toward a solidifying Republican advantage, especially as rural and exurban turnout rises and Democratic support in minority communities faces new challenges.

**Narrative Note:**
> *NC-07’s transformation is driven by the dramatic realignment of Robeson County and the Lumbee tribe, as well as broader rural shifts. While Fayetteville and Wilmington anchor Democratic strength, the district’s rural and Native areas now form a solid Republican bloc, making NC-07 a microcosm of eastern North Carolina’s changing political landscape.*

---

## Trends in NC-08 (Lexington / Salisbury / Union County)

**Summary:**  
NC-08 covers the exurban fringes of Charlotte, the fast-growing Piedmont Triad exurbs (including Davidson County), and a swath of rural south-central North Carolina. The district includes Union County—a very fast-growing Charlotte exurb due to its proximity to the city, but one that has barely shifted in federal elections—as well as Stanly, Montgomery, Anson, Rowan, parts of Cabarrus and most of Richmond counties. Union and Davidson counties anchor the district’s rapid population growth, driven by new housing developments and an influx of families seeking affordable living near Charlotte and the Triad. The population is predominantly white, suburban, and exurban, with a mix of small towns and rural communities. GOP margins have grown as rural and exurban voters consolidate behind the party, and conservative newcomers from the Charlotte metro area reinforce Republican dominance. Democrats have struggled to make inroads, with the district’s political culture shaped by suburban growth, evangelical churches, and a strong tradition of conservative politics. Major population centers in the district include Lexington, Salisbury, Albemarle, and rapidly growing Union County suburbs such as Monroe and Indian Trail—both of which have seen explosive growth as families move outward from Charlotte. This suburban expansion has made Union County one of the fastest-growing in the state, yet it remains solidly Republican in federal elections. Other notable communities include Thomasville on the district’s northern fringe, further illustrating the geographic and demographic diversity of NC-08.

The district’s economy is anchored by manufacturing, logistics, agriculture, and retail, with many residents commuting to jobs in Charlotte, the Triad, or local industrial parks. Towns like Monroe, Indian Trail, and Thomasville serve as key commuter hubs, while Lexington and Salisbury have long histories in furniture, textiles, and food processing. This blend of traditional industries and suburban growth shapes both the economic landscape and the political culture of NC-08.

**Key Trends:**
- **President:**
    - 2008: McCain 62.16%, Obama 36.47% (R+25.69)
    - 2012: Romney 64.94%, Obama 35.06% (R+29.88)
    - 2016: Trump 66.36%, Clinton 30.14% (R+36.22)
    - 2020: Trump 66.35%, Biden 32.34% (R+34.01)
    - 2024: Trump 67.14%, Harris 31.90% (R+35.24)
- **Governor:**
    - 2008: McCrory 61.20%, Perdue 36.36% (R+24.84)
    - 2012: McCrory 69.89%, Dalton 28.39% (R+41.5)
    - 2016: McCrory 64.36%, Cooper 33.42% (R+30.94)
    - 2020: Forest 63.00%, Cooper 35.67% (R+27.33)
    - 2024: Robinson 55.22%, Stein 39.28% (R+15.94)
- **Senate:**
    - 2008: Dole 54.63%, Hagan 41.58% (R+13.05)
    - 2010: Burr 65.95%, Marshall 31.79% (R+34.16)
    - 2014: Tillis 61.98%, Hagan 33.38% (R+28.6)
    - 2016: Burr 66.02%, Ross 29.67% (R+36.35)
    - 2020: Tillis 63.91%, Cunningham 31.67% (R+32.24)
    - 2022: Budd 67.51%, Beasley 30.34% (R+37.17)
- **Attorney General:**
    - 2016: Newton 64.83%, Stein 35.17% (R+29.66)
    - 2020: O'Neill 65.61%, Stein 34.39% (R+31.22)
    - 2024: Bishop 64.43%, Jackson 35.57% (R+28.86)
- **Lt Governor:**
    - 2016: Forest 67.86%, Coleman 29.47% (R+38.39)
    - 2020: Robinson 67.75%, Holley 32.25% (R+35.5)
    - 2024: Weatherman 63.31%, Hunt 33.81% (R+29.5)
- **Supreme Court:**
    - 2022: Dietz 65.79%, Inman 34.21% (R+31.58)
    - 2022.1: Allen 65.49%, Ervin 34.51% (R+30.98)
    - 2024: Griffin 65.79%, Riggs 34.21% (R+31.58)

**Analytical Notes:**
> **President:** Republican margins have grown dramatically, from McCain +26 in 2008 to Trump +40 in 2024. The district’s deep manufacturing and agricultural roots—especially in Hickory, Shelby, Lincolnton, and Morganton—have fostered a working-class, socially conservative electorate. While population growth is slow in many areas, the Lake Norman corridor in southern Iredell and eastern Lincoln counties has seen rapid suburban expansion, attracting new families and retirees. However, these newcomers have largely reinforced the GOP’s dominance, rather than shifting the district’s political balance. Democratic support is limited to a few urban precincts, with Lenoir-Rhyne University in Hickory standing out as one of the district’s few blue pockets, but these are overwhelmed by the rural, exurban, and suburban vote.
> **Governor:** The GOP’s dominance is rooted in the district’s economic legacy and cultural conservatism, with evangelical churches, small-town traditions, and a strong sense of local identity shaping political attitudes. Even as Charlotte’s influence creeps westward and suburban growth accelerates along Lake Norman, Republican margins remain above 20 points in every cycle, and the district remains a Republican stronghold.
> **Senate:** The region’s blend of old-line small towns and dynamic new suburbs produces some of the largest GOP margins in the state, with working-class and suburban voters alike supporting Republican candidates by wide margins. High turnout and party loyalty in both midterm and presidential years reinforce the district’s deep red identity.
> **Attorney General:** Down-ballot races mirror the top of the ticket, with the district’s economic and cultural cohesion ensuring continued Republican dominance. Even as the local economy diversifies and new residents arrive, Democratic candidates have struggled to gain traction outside a handful of urban and university precincts.
> **Lt Governor:** GOP candidates have posted landslide wins, with margins above 34 points in every cycle. The race closely tracks the presidential and Senate results, with the district’s rural, exurban, and suburban voters providing a reliable base for Republican candidates.
> **Supreme Court:** Republican candidates have swept all recent Supreme Court races, with margins above 36 points, underscoring the district’s deep red identity. The results reflect both high partisan loyalty and the district’s strong alignment with the NCGOP’s statewide coalition, making NC-10 a linchpin for Republican judicial victories.

---

## Trends in NC-11 (Asheville / Hendersonville / Brevard)

**Summary:**  
NC-11 encompasses the heart of western North Carolina, including Asheville, Hendersonville, Brevard, and the surrounding mountain counties. The district is geographically vast and diverse, with Asheville serving as a progressive, artsy urban hub surrounded by deeply conservative rural and small-town communities. The economy is driven by tourism, outdoor recreation, healthcare, and higher education, with Asheville’s rapid growth and cultural vibrancy contrasting with the slower pace and traditional values of the outlying counties. The region is home to a significant retiree population, a growing Latino community, and a strong tradition of localism. While Asheville and a few nearby precincts vote Democratic, the rest of the district is solidly Republican, making NC-11 a classic example of the urban-rural divide in North Carolina politics. Jackson County, home to Western Carolina University, is a notable swing area but has trended Republican in recent cycles. The rest of the district—comprising counties like Haywood, Macon, Rutherford, Swain, Transylvania, Madison, Yancey, Polk, Graham, Cherokee, and Clay—remains deeply conservative and reliably Republican, reinforcing the stark urban-rural divide that defines NC-11.

**Key Trends:**
- **President:**
    - 2008: McCain (R) vs. Obama (D): McCain (R) +5.75 (52.01% to 46.26%)
    - 2012: Romney (R) vs. Obama (D): Romney (R) +10.2 (55.10% to 44.90%)
    - 2016: Trump (R) vs. Clinton (D): Trump (R) +15.13 (55.19% to 40.06%)
    - 2020: Trump (R) vs. Biden (D): Trump (R) +10.13 (54.28% to 44.15%)
    - 2024: Trump (R) vs. Harris (D): Trump (R) +8.78 (53.78% to 45.00%)
- **Governor:**
    - 2008: Perdue (D) vs. McCrory (R): Perdue (D) +5.46 (50.85% to 45.39%)
    - 2012: McCrory (R) vs. Dalton (D): McCrory (R) +13.48 (55.22% to 41.74%)
    - 2016: McCrory (R) vs. Cooper (D): McCrory (R) +4.53 (50.77% to 46.24%)
    - 2020: Forest (R) vs. Cooper (D): Forest (R) +4 (51.21% to 47.21%)
    - 2024: Stein (D) vs. Robinson (R): Stein (D) +8.26 (51.86% to 43.60%)
- **Senate:**
    - 2008: Hagan (D) vs. Dole (R): Hagan (D) +3.89 (50.02% to 46.13%)
    - 2010: Burr (R) vs. Marshall (D): Burr (R) +14.87 (56.04% to 41.17%)
    - 2014: Tillis (R) vs. Hagan (D): Tillis (R) +5.19 (50.30% to 45.11%)
    - 2016: Burr (R) vs. Ross (D): Burr (R) +12.49 (54.17% to 41.68%)
    - 2020: Tillis (R) vs. Cunningham (D): Tillis (R) +9.29 (52.55% to 43.26%)
    - 2022: Budd (R) vs. Beasley (D): Budd (R) +8.03 (52.71% to 44.68%)
- **Attorney General:**
    - 2016: Newton (R) vs. Stein (D): Newton (R) +8.06 (54.03% to 45.97%)
    - 2020: O'Neill (R) vs. Stein (D): O'Neill (R) +8.72 (54.36% to 45.64%)
    - 2024: Bishop (R) vs. Jackson (D): Bishop (R) +3.8 (51.90% to 48.10%)
- **Lt Governor:**
    - 2016: Forest (R) vs. Coleman (D): Forest (R) +12.91 (54.63% to 41.72%)
    - 2020: Robinson (R) vs. Holley (D): Robinson (R) +11.76 (55.88% to 44.12%)
    - 2024: Weatherman (R) vs. Hunt (D): Weatherman (R) +4.49 (50.85% to 46.36%)
- **Supreme Court:**
    - 2022: Inman (D) vs. Dietz (R): Dietz (R) +9.78  (54.89% to 45.11%)
    - 2022.1: Ervin (D) vs. Allen (R): Allen (R) +7.84 (53.92% to 46.08%)
    - 2024: Griffin (R) vs. Riggs (D): Griffin (R) +6 (53.00% to 47.00%)

**Analytical Notes:**
> **President:** NC-11’s presidential margins have shifted from McCain (R) +5.75 in 2008 to Trump (R) +8.78 in 2024, with the GOP’s strength anchored in rural counties like Macon, Haywood, and Cherokee, while Asheville and Jackson County (home to Western Carolina University) provide Democratic counterweights. Buncombe County, anchored by Asheville, continues to trend blue, but the rest of the district remains solidly Republican. The 2024 race was further complicated by Hurricane Helene, which disrupted turnout in several mountain counties.
> **Governor:** Margins have swung from Perdue (D) +5.46 in 2008 to Stein (D) +8.26 in 2024, with Democratic strength in Asheville and Jackson County offset by Republican dominance elsewhere. The 2024 result reflected both high urban turnout and the hurricane’s impact on rural voting.
> **Senate:** Senate races have ranged from Hagan (D) +3.89 in 2008 to Budd (R) +8.03 in 2022, with close margins in Buncombe and Jackson but strong GOP wins in the rest of the district. The region’s economic anxiety and cultural conservatism continue to drive Republican support.
> **Attorney General:** Margins have narrowed from Newton (R) +8.06 in 2016 to Bishop (R) +3.8 in 2024, with Democratic gains in Asheville and Jackson County. The 2024 contest was especially close due to high student and faculty turnout at WCU and weather disruptions.
> **Lt Governor:** The GOP’s advantage has shrunk from Forest (R) +12.91 in 2016 to Weatherman (R) +4.49 in 2024, with Democratic strength in urban and university precincts. The hurricane’s timing may have suppressed rural turnout.
> **Supreme Court:** Recent races have been competitive: Dietz (R) +9.78 in 2022, Allen (R) +7.84 in 2022.1, and Griffin (R) +6 in 2024. Democratic support is concentrated in Asheville and Jackson, while the rest of the district remains reliably Republican. The 2024 judicial races also saw localized turnout effects from Hurricane Helene.

**Narrative Note:**  
> *NC-11 is North Carolina’s mountain district, stretching from the vibrant, progressive city of Asheville through the Blue Ridge and Smoky Mountains to some of the state’s most rural and traditional communities. The district’s political identity is defined by a sharp urban-rural divide: Asheville and its suburbs are Democratic strongholds, while the surrounding counties—rooted in Appalachian culture, evangelical faith, and economic conservatism—remain deeply Republican. In recent years, population growth, tourism, and an influx of retirees have diversified the economy and electorate, making NC-11 one of the state’s most competitive and closely watched districts. Recent cycles have seen some of the closest margins in the state, with high turnout in Asheville and Jackson County offset by overwhelming Republican strength in the rest of the district. Jackson County, home to Western Carolina University, stands out as less Republican-leaning than its neighbors, with a more competitive political climate and a growing student and faculty population that bolsters Democratic margins. The 2020 and 2022 cycles were especially competitive, with Democrats making gains in Buncombe and Jackson but falling short districtwide. The district’s turnout is often among the highest in North Carolina, reflecting both strong civic engagement and the intensity of the urban-rural divide. The 2024 elections were further shaped by the impact of Hurricane Helene, which disrupted turnout and campaign activity in several mountain counties, adding another layer of complexity to an already competitive landscape. As Asheville continues to grow and diversify, NC-11 is likely to remain a closely watched battleground, but for now, the GOP’s rural base keeps the district reliably Republican outside the city core.*


## Trends in NC-12 (Uptown Charlotte / Davidson / Concord)

**Summary:**  
NC-12 is centered on Uptown Charlotte and its northern suburbs, including Davidson, Concord, and parts of Cabarrus and Mecklenburg counties. The district is highly urban, racially and ethnically diverse, and rapidly growing, with a large Black population and significant Latino and Asian communities. Charlotte’s status as a major banking, tech, and healthcare hub drives economic growth and attracts young professionals from across the country. The district’s political culture is shaped by progressive activism, high educational attainment, and a strong tradition of civic engagement. NC-12 is one of the most Democratic districts in the state, with the party routinely winning by 25 points or more in federal and statewide races. Republican support is limited to a few suburban precincts, but the overall trend is one of growing Democratic strength, fueled by demographic change and urbanization.

**Key Trends:**
- **President:**
    - 2008: Obama (D) vs. McCain (R): Obama (D) +23.43 (61.29% to 37.86%)
    - 2012: Obama (D) vs. Romney (R): Obama (D) +24.1 (62.05% to 37.95%)
    - 2016: Clinton (D) vs. Trump (R): Clinton (D) +24.68 (60.23% to 35.55%)
    - 2020: Biden (D) vs. Trump (R): Biden (D) +30.1 (64.24% to 34.14%)
    - 2024: Harris (D) vs. Trump (R): Harris (D) +28.97 (63.62% to 34.65%)
- **Governor:**
    - 2008: Perdue (D) vs. McCrory (R): Perdue (D) +6.26 (52.15% to 45.89%)
    - 2012: Dalton (D) vs. McCrory (R): Dalton (D) +3.62 (50.94% to 47.32%)
    - 2016: Cooper (D) vs. McCrory (R): Cooper (D) +25.84 (61.62% to 35.78%)
    - 2020: Cooper (D) vs. Forest (R): Cooper (D) +33.66 (65.87% to 32.21%)
    - 2024: Stein (D) vs. Robinson (R): Stein (D) +42.97 (68.95% to 25.98%)
- **Senate:**
    - 2008: Hagan (D) vs. Dole (R): Hagan (D) +27.01 (61.99% to 34.98%)
    - 2010: Marshall (D) vs. Burr (R): Marshall (D) +9.1 (53.67% to 44.57%)
    - 2014: Hagan (D) vs. Tillis (R): Hagan (D) +22.95 (60.05% to 37.10%)
    - 2016: Ross (D) vs. Burr (R): Ross (D) +21.16 (58.61% to 37.45%)
    - 2020: Cunningham (D) vs. Tillis (R): Cunningham (D) +26.86 (61.00% to 34.14%)
    - 2022: Beasley (D) vs. Budd (R): Beasley (D) +26.68 (62.21% to 35.53%)
- **Attorney General:**
    - 2016: Stein (D) vs. Newton (R): Stein (D) +25.92 (62.96% to 37.04%)
    - 2020: Stein (D) vs. O'Neill (R): Stein (D) +30.18 (65.09% to 34.91%)
    - 2024: Jackson (D) vs. Bishop (R): Jackson (D) +34.98 (67.49% to 32.51%)
- **Lt Governor:**
    - 2016: Coleman (D) vs. Forest (R): Coleman (D) +19.17 (57.95% to 38.78%)
    - 2020: Holley (D) vs. Robinson (R): Holley (D) +28.16 (64.08% to 35.92%)
    - 2024: Hunt (D) vs. Weatherman (R): Hunt (D) +33.43 (65.28% to 31.85%)
- **Supreme Court:**
    - 2022: Inman (D) vs. Dietz (R): Inman (D) +24.74 (62.37% to 37.63%)
    - 2022.1: Ervin (D) vs. Allen (R): Ervin (D) +24.9 (62.45% to 37.55%)
    - 2024: Riggs (D) vs. Griffin (R): Riggs (D) +31.9 (65.95% to 34.05%)

**Analytical Notes:**
> **President:** NC-12 has become a Democratic stronghold, with margins growing from Obama (D) +23.4 in 2008 to Harris (D) +29 in 2024. The district’s diverse, urban electorate—anchored by Charlotte’s Black, Latino, and Asian communities—has driven consistent Democratic gains, especially as young professionals and new residents move into Uptown and the northern suburbs. Republican support is now limited to a handful of suburban precincts.
> **Governor:** Democratic margins have surged, from Perdue (D) +6.3 in 2008 to Stein (D) +43 in 2024, reflecting both demographic change and the growing influence of progressive activism. The district’s high educational attainment and civic engagement have made it a bellwether for statewide Democratic strength.
> **Senate:** Senate races have consistently favored Democrats, with margins above 20 points in every cycle except 2010. The district’s urban core and diverse suburbs provide a deep well of Democratic votes, while Republican candidates struggle to gain traction outside a few outlying areas.
> **Attorney General:** Democratic candidates have posted landslide wins, with margins rising from Stein (D) +26 in 2016 to Jackson (D) +35 in 2024. The trend mirrors the top of the ticket, with strong support from Black, Latino, and college-educated voters.
> **Lt Governor:** The Democratic advantage has widened, from Coleman (D) +19 in 2016 to Hunt (D) +33 in 2024, as the district’s urban and suburban voters continue to shift left. The race closely tracks presidential and gubernatorial results.
> **Supreme Court:** Judicial races have also become more lopsided, with Democratic margins above 24 points in every recent contest and Riggs (D) +32 in 2024. The results underscore the district’s deep blue identity and the growing influence of Charlotte’s professional and minority communities.

**Narrative Note:**  
> *NC-12 is the beating heart of urban North Carolina, centered on Uptown Charlotte and its rapidly growing northern suburbs. The district’s political culture is shaped by its racial and ethnic diversity—including one of the largest African American populations in the South, second only to Atlanta—high educational attainment, and status as a national banking, tech, and healthcare hub—earning Charlotte a reputation as "NYC lite" for its concentration of financial sector jobs and cosmopolitan energy. Charlotte’s vibrant arts scene, progressive activism, and influx of young professionals have transformed NC-12 into one of the most Democratic districts in the state. While Republican support lingers in a few suburban pockets, the overall trend is one of growing Democratic strength, fueled by demographic change, urbanization, and a strong tradition of civic engagement. Notably, the district also includes Concord, Harrisburg, and Kannapolis in Cabarrus County, where left-trending suburbs have contributed to widening Democratic margins and reflect the broader suburban shift. The district’s future will be shaped by continued population growth, economic dynamism, and the evolving political identity of Charlotte’s diverse communities.*

---

## Trends in NC-13 (South Wake Suburbs / Johnston / Wayne)

**Summary:**  
NC-13 is one of North Carolina’s most competitive and rapidly changing districts, encompassing the booming southern Wake County suburbs (including Fuquay-Varina, Holly Springs, and Garner), nearly all of Johnston County, most of Harnett County, and the western portion of Wayne County—including Goldsboro. The district’s electorate is a true cross-section of modern North Carolina: suburban professionals and young families in Wake and Johnston, rural and small-town conservatives in Harnett, and a significant Black population in both the Raleigh area of Wake County and in Goldsboro. Johnston County is among the fastest-growing in the state, drawing new residents from the Triangle and beyond, while Harnett and Wayne retain a more traditional, small-city and rural character. The result is a district where margins are razor-thin, turnout is among the highest in the state, and both parties invest heavily in organizing, persuasion, and coalition-building. NC-13’s political identity is shaped by rapid demographic change, suburbanization, and the ongoing realignment of rural and urban voters, making it a perennial battleground and a bellwether for statewide trends.

**Key Trends:**
- **President:**
    - 2008: McCain (R) vs. Obama (D): McCain (R) +0.16 (49.52% to 49.36%)
    - 2012: Romney (R) vs. Obama (D): Romney (R) +2.98 (51.49% to 48.51%)
    - 2016: Trump (R) vs. Clinton (D): Trump (R) +2.34 (48.98% to 46.64%)
    - 2020: Biden (D) vs. Trump (R): Biden (D) +1.69 (49.97% to 48.28%)
    - 2024: Harris (D) vs. Trump (R): Harris (D) +0.96 (49.76% to 48.80%)
- **Governor:**
    - 2008: Perdue (D) vs. McCrory (R): Perdue (D) +2.07 (49.61% to 47.54%)
    - 2012: McCrory (R) vs. Dalton (D): McCrory (R) +11.09 (54.42% to 43.33%)
    - 2016: Cooper (D) vs. McCrory (R): Cooper (D) +0.48 (49.24% to 48.76%)
    - 2020: Cooper (D) vs. Forest (R): Cooper (D) +7.92 (53.19% to 45.27%)
    - 2024: Stein (D) vs. Robinson (R): Stein (D) +20.77 (57.57% to 36.80%)
- **Senate:**
    - 2008: Hagan (D) vs. Dole (R): Hagan (D) +5.14 (51.13% to 45.99%)
    - 2010: Burr (R) vs. Marshall (D): Burr (R) +12.43 (55.22% to 42.79%)
    - 2014: Tillis (R) vs. Hagan (D): Tillis (R) +2.37 (49.48% to 47.11%)
    - 2016: Burr (R) vs. Ross (D): Burr (R) +5.01 (50.89% to 45.88%)
    - 2020: Cunningham (D) vs. Tillis (R): Cunningham (D) +0.3 (47.79% to 47.49%)
    - 2022: Beasley (D) vs. Budd (R): Beasley (D) +1.47 (49.56% to 48.09%)
- **Attorney General:**
    - 2016: Stein (D) vs. Newton (R): Stein (D) +0.62 (50.31% to 49.69%)
    - 2020: Stein (D) vs. O'Neill (R): Stein (D) +3.5 (51.75% to 48.25%)
    - 2024: Jackson (D) vs. Bishop (R): Jackson (D) +6.88 (53.44% to 46.56%)
- **Lt Governor:**
    - 2016: Forest (R) vs. Coleman (D): Forest (R) +6.35 (51.80% to 45.45%)
    - 2020: Robinson (R) vs. Holley (D): Robinson (R) +0.5 (50.25% to 49.75%)
    - 2024: Hunt (D) vs. Weatherman (R): Hunt (D) +6.2 (51.55% to 45.35%)
- **Supreme Court:**
    - 2022: Inman (D) vs. Dietz (R): Inman (D) +1.1 (50.55% to 49.45%)
    - 2022.1: Ervin (D) vs. Allen (R): Ervin (D) +0.24 (50.12% to 49.88%)
    - 2024: Riggs (D) vs. Griffin (R): Riggs (D) +4.08 (52.04% to 47.96%)

**Analytical Notes:**
> **President:** NC-13 is a true swing district, with margins under 3 points in every cycle since 2008. The explosive growth of Johnston County—especially in Clayton and along the I-40 corridor—has brought an influx of young families, commuters, and new businesses, shifting many precincts from reliably Republican to highly competitive. Southern Wake suburbs like Fuquay-Varina and Holly Springs have also trended left, while Harnett and rural western Wayne remain GOP strongholds. Black and Latino communities in Goldsboro and the Raleigh area of Wake County provide a crucial Democratic base, and high turnout in these areas has been decisive in recent cycles. The 2020 and 2024 elections saw razor-thin Democratic wins, with national issues and local demographic change both playing major roles.
> **Governor:** Gubernatorial races have swung between the parties, but the Democratic surge in Johnston and Wake since 2016 has been dramatic. Stein’s 2024 margin (+20.8) was driven by record turnout in suburban precincts, while Harnett and rural Wayne continued to anchor the Republican vote. Stein's 2024 blowout could've been enhanced by Mark Robinson's candidate quality issues and September surprise alienating unaffilated swing voters, which matter a lot in a district like this. The district’s mix of fast-growing exurbs and traditional rural communities makes it a bellwether for statewide trends.
> **Senate:** Senate contests have been highly competitive, with margins under 6 points in every cycle since 2008. Democratic gains in Johnston and Wake have been offset by strong Republican performance in Harnett and Wayne. Beasley’s narrow win in 2022 (+1.5) underscores the volatility and importance of both suburban and rural turnout.
> **Attorney General:** Margins have shifted from a near-tie in 2016 (Stein +0.6) to a clear Democratic edge in 2024 (Jackson +6.9), as the party consolidates support in growing suburbs and among minority communities in Goldsboro and southern Wake. The race has become a bellwether for broader partisan trends, with local issues like public safety and education playing a larger role.
> **Lt Governor:** The district has flipped between parties, with the Democratic margin growing to 6.2 in 2024 as suburban and minority turnout increased. Johnston County’s rapid development and the increasing diversity of Wake’s suburbs have played a key role, while Harnett and rural Wayne remain Republican anchors. Down-ballot races increasingly mirror the top of the ticket.
> **Supreme Court:** Judicial races have been extremely close, with Democratic margins ranging from 0.2 to 4.1 points. The results reflect the district’s competitive nature, the impact of high turnout in suburban and minority precincts, and the importance of every vote in a district where partisan control is always up for grabs. Local legal issues and candidate backgrounds have also influenced outcomes, making these races especially unpredictable.

---

## Trends in NC-14 (South Charlotte / Ballantyne / Gastonia)

**Summary:**  
NC-14, covering the southern and western suburbs of Charlotte, is a rapidly evolving district that has seen significant Democratic gains in recent cycles. The district includes parts of Mecklenburg and Gaston counties, encompassing fast-growing suburban communities like Matthews, Pineville, Ballantyne, Belmont, and Mount Holly. Population growth has been fueled by an influx of younger families, professionals, and a more racially and ethnically diverse population, drawn by the area’s economic opportunities, top-rated schools, and high quality of life. Once reliably Republican, the district’s political landscape has shifted as suburbanization and demographic change have eroded the GOP’s advantage, especially in Mecklenburg County. Gaston County remains more conservative, but Democratic candidates have made inroads in its suburban precincts, particularly in Belmont and Mount Holly. The district’s results reflect the broader trend of suburban areas in North Carolina moving toward the Democratic Party, with high turnout, competitive down-ballot races, and a growing base of college-educated, nonwhite, and younger voters making NC-14 one of the state’s most closely watched and competitive districts for the future.

**Key Trends:**
- **President:**
    - 2008: Obama (D) vs. McCain (R): Obama (D) +4.13 (51.60% to 47.47%)
    - 2012: Obama (D) vs. Romney (R): Obama (D) +1.7 (50.85% to 49.15%)
    - 2016: Clinton (D) vs. Trump (R): Clinton (D) +9.72 (52.35% to 42.63%)
    - 2020: Biden (D) vs. Trump (R): Biden (D) +16.36 (57.33% to 40.97%)
    - 2024: Harris (D) vs. Trump (R): Harris (D) +15.36 (57.00% to 41.64%)
- **Governor:**
    - 2008: McCrory (R) vs. Perdue (D): McCrory (R) +19.24 (58.58% to 39.34%)
    - 2012: McCrory (R) vs. Dalton (D): McCrory (R) +22.08 (60.15% to 38.07%)
    - 2016: Cooper (D) vs. McCrory (R): Cooper (D) +9.92 (53.73% to 43.81%)
    - 2020: Cooper (D) vs. Forest (R): Cooper (D) +19.17 (58.73% to 39.56%)
    - 2024: Stein (D) vs. Robinson (R): Stein (D) +34.41 (64.44% to 30.03%)
- **Senate:**
    - 2008: Hagan (D) vs. Dole (R): Hagan (D) +8.36 (52.55% to 44.19%)
    - 2010: Burr (R) vs. Marshall (D): Burr (R) +14.54 (56.22% to 41.68%)
    - 2014: Hagan (D) vs. Tillis (R): Hagan (D) +1.26 (49.04% to 47.78%)
    - 2016: Ross (D) vs. Burr (R): Ross (D) +2.07 (49.07% to 47.00%)
    - 2020: Cunningham (D) vs. Tillis (R): Cunningham (D) +10.74 (53.21% to 42.47%)
    - 2022: Beasley (D) vs. Budd (R): Beasley (D) +15.59 (56.72% to 41.13%)
- **Attorney General:**
    - 2016: Stein (D) vs. Newton (R): Stein (D) +8.32 (54.16% to 45.84%)
    - 2020: Stein (D) vs. O'Neill (R): Stein (D) +13.88 (56.94% to 43.06%)
    - 2024: Jackson (D) vs. Bishop (R): Jackson (D) +22.98 (61.49% to 38.51%)
- **Lt Governor:**
    - 2016: Forest (R) vs. Coleman (D): Forest (R) +0.72 (48.69% to 47.97%)
    - 2020: Holley (D) vs. Robinson (R): Holley (D) +11.28 (55.64% to 44.36%)
    - 2024: Hunt (D) vs. Weatherman (R): Hunt (D) +19.23 (58.28% to 39.05%)
- **Supreme Court:**
    - 2022: Inman (D) vs. Dietz (R): Inman (D) +12.62 (56.31% to 43.69%)
    - 2022.1: Ervin (D) vs. Allen (R): Ervin (D) +13.6 (56.80% to 43.20%)
    - 2024: Riggs (D) vs. Griffin (R): Riggs (D) +17.72 (58.86% to 41.14%)

**Analytical Notes:**
> **President:** NC-14 has shifted dramatically toward the Democrats, with margins growing from Obama (D) +4.1 in 2008 to Harris (D) +15.4 in 2024. The transformation is driven by rapid suburban growth, an influx of college-educated and nonwhite residents, and changing attitudes among younger families and professionals. Mecklenburg County precincts, especially in Ballantyne, Matthews, and Pineville, have trended sharply left, while Gaston County remains a Republican anchor—GOP candidates still routinely receive 60% or more of the vote in the Gaston portion, especially in Gastonia and surrounding exurbs. However, Democratic candidates have made inroads in Belmont, Mount Holly, and other Gaston County suburbs, narrowing margins and reflecting the broader suburban shift.
> **Governor:** Once a Republican stronghold, the district has seen a dramatic Democratic surge in gubernatorial races, with Stein (D) winning by over 34 points in 2024. High turnout in suburban Mecklenburg and growing diversity have fueled this shift, while Gaston’s suburbs are increasingly competitive, though the GOP still dominates in Gastonia proper.
> **Senate:** Senate races have followed the same pattern, with Democratic margins rising from single digits to over 15 points in 2022. The district’s mix of affluent suburbs, diverse communities, and shifting cultural attitudes has made it a Democratic stronghold in federal races, but Gaston County continues to deliver strong Republican totals, especially in Gastonia.
> **Attorney General:** Democratic candidates have posted double-digit wins in every cycle since 2016, with Jackson (D) winning by nearly 23 points in 2024. The trend mirrors the top of the ticket, with strong support from college-educated, minority, and younger voters in Mecklenburg, while Gaston’s GOP base remains resilient.
> **Lt Governor:** The Democratic advantage has widened, from a near-tie in 2016 to a 19-point win in 2024, as suburban and minority turnout has surged. The race closely tracks presidential and gubernatorial results, with Gaston’s suburbs playing a key role in the margin, but Gastonia and rural Gaston precincts still provide a solid Republican floor.
> **Supreme Court:** Judicial races have become increasingly lopsided, with Democratic margins above 12 points in every recent contest and Riggs (D) +17.7 in 2024. The results underscore the district’s deep blue identity and the growing influence of Charlotte’s professional and minority communities, as well as the competitive but still Republican-leaning nature of Gaston’s suburban and exurban precincts.

**Narrative Note:**  
> *NC-14 is a textbook example of suburban realignment in North Carolina, covering the fast-growing southern and western suburbs of Charlotte and extending into Gaston County. The district’s political culture is shaped by rapid population growth, economic opportunity, and increasing racial and ethnic diversity. Once a Republican bastion, NC-14 has become a Democratic stronghold as college-educated, nonwhite, and younger voters reshape the electorate. Mecklenburg County’s suburbs—especially Ballantyne, Matthews, and Pineville—have trended sharply left, while Gaston County, though still more conservative, is no longer immune to these changes. Gastonia remains a GOP stronghold, with Republicans still winning large majorities there, but Democratic candidates have made steady gains in Belmont, Mount Holly, and other Gaston suburbs. High turnout, competitive down-ballot races, and a dynamic, diverse population make NC-14 one of the most closely watched and politically dynamic districts in the state, with its future likely to mirror the broader trends of suburban America.*

---

## Analysis Notes
- Districts with major partisan shifts will be highlighted in the narrative.
- Split-ticket voting and outlier districts will be discussed.
- Visualizations (maps, charts) may be added for clarity.
- Cabarrus and Alamance counties, while still leaning Republican, have become more competitive in recent cycles (2020 margin: Cabarrus R+9.4, Alamance R+8.4; 2024 margin: Cabarrus R+7.7, Alamance R+8.1) as unaffiliated registration has surpassed both major parties and suburban growth accelerates due to proximity to Charlotte, the Triad, and the Triangle.
    - In 2020, Trump carried Cabarrus County 53.94% to 44.50%, but it was also the first time since 2008 that a Democrat cracked 40% there, signaling increased competitiveness.
    - In 2020, Trump carried Alamance County 53.50% to 45.10%, marking the first time since 2008 that a Democrat cracked 45% in the county (Obama received 44.94% that year).
    - In 2024, Trump carried Cabarrus County 53.03% to 45.34% (R+7.7), continuing the trend of narrowing margins.
    - In 2024, Trump carried Alamance County 53.36% to 45.22% (R+8.1) Again, Democrats maintained their improved share from 2020.
    - Notably, the Democratic share in Alamance County was nearly identical in both 2020 (45.10%) and 2024 (45.22%), a pattern recognized by the analyst. This statistical similarity across cycles highlights the value of close data examination and underscores the importance of tracking subtle but persistent trends in competitive counties.
    - The influx of new industries and residents has also contributed to rising voter registration and turnout in both counties, with unaffiliated voters now outnumbering both Democrats and Republicans. In recent statewide elections, shifts in Cabarrus and Alamance have been pivotal to overall margins, underscoring their growing importance in North Carolina's political landscape. These trends mirror broader national patterns of suburban realignment and the transformation of formerly safe Republican counties into competitive battlegrounds.
    - In Cabarrus County, fast-growing communities include Concord, Kannapolis, and Harrisburg, each seeing significant residential and commercial development. In Alamance County, Graham, Burlington, and Mebane are expanding rapidly, with Mebane in particular attracting new industry and commuters due to its location along the I-40/I-85 corridor. Notably, a Buc-ee’s is scheduled to open in Mebane in late 2026 or early 2027, highlighting the area’s commercial growth and rising regional profile. These cities and towns exemplify the suburban growth and demographic change driving the region's political transformation.

---
