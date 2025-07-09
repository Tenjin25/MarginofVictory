# North Carolina Congressional Realignment Case Study (2008–2024)

## Overview
This case study analyzes partisan realignment and electoral trends in North Carolina's congressional districts using historical election data (2008–2024) projected onto the 2023-2025 14-district map. By applying past presidential and statewide results to the new map, we can track how each district's political lean has shifted over time, regardless of how many districts existed in the original election year.

**Note:** North Carolina had 13 districts prior to the 2020 census. All historical results are retrofitted to the 2023-2025 14-district map for consistency and comparative analysis. As of the 2025 Congress, the map has been redrawn again due to ongoing litigation and partisan gerrymandering, so the current map may differ from the one used in this analysis. This case study uses the 2023-2025 map as a stable reference point for historical comparison, but readers should be aware that district boundaries and numbers may change in future cycles.

---

## Data Sources
- Official North Carolina election results (2008–2024)
- Datasets: `2008 Pres Statistics.csv`, `2012 Pres Statistics.csv`, `2016 Pres Statistics.csv`, `2020 Pres Statistics.csv`, `2024 Pres Statistics.csv`, etc.
- Map reference: 2022+ congressional map (14 districts)

---

## Methodology
- Each dataset contains district-level Democratic, Republican, and Other vote shares for a given election year, plus a "Statewide" row for context.
- District numbers correspond to the current 14-district map, even for years when only 13 districts existed.
- This approach allows for direct comparison of partisan trends and realignment across cycles.

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
| 3         | Eastern / Crystal Coast / Carteret        | 41.00   | 57.79    |
| 4         | Durham / Chapel Hill / RTP / Orange       | 64.87   | 34.03    |
| 5         | Northwest / Foothills / Wilkes            | 42.55   | 55.95    |
| 6         | Greensboro / Piedmont Triad / High Point  | 55.34   | 43.60    |
| 7         | Fayetteville / Sandhills / Robeson        | 47.47   | 51.26    |
| 8         | South Central / Union / Anson             | 36.47   | 62.16    |
| 9         | Randolph / Fort Bragg / Moore             | 48.60   | 50.17    |
| 10        | Western Foothills / Nw Gaston / Cleveland | 36.22   | 62.38    |
| 11        | Asheville / Mountains / Buncombe          | 46.26   | 52.01    |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 61.29   | 37.86    |
| 13        | Triangle Suburbs / Johnston / Wayne       | 49.36   | 49.52    |
| 14        | Charlotte South / Ballantyne / Gaston     | 51.60   | 47.47    |
| Statewide | —                                         | 49.51    | 49.28     |

| Statewide Winner | Margin |
|------------------|--------|
| Obama (D)        | +0.23  |

*In 2008, Barack Obama won North Carolina statewide by approximately 0.23 percentage points (49.51% to 49.28%).*

> **Note:** The 2008 election marked North Carolina's emergence as a true swing state—a status it has maintained through subsequent cycles due to rapid population growth, demographic change, and ongoing partisan realignment. This context is essential for understanding the competitive nature of recent elections and the evolving political landscape in the state.

---

## District-Level 2008 Gubernatorial Results

| District | Region                                    | Perdue (D) % | McCrory (R) % |
|----------|-------------------------------------------|--------------|---------------|
| 1        | Northeast / Inner Coastal Plain           | 63.24        | 35.10         |
| 2        | Raleigh Metro / North Wake                | 50.17        | 45.87         |
| 3        | Eastern / Crystal Coast / Carteret        | 53.28        | 44.22         |
| 4        | Durham / Chapel Hill / RTP / Orange       | 62.49        | 33.67         |
| 5        | Northwest / Foothills / Wilkes            | 45.74        | 51.06         |
| 6        | Greensboro / Piedmont Triad / High Point  | 55.94        | 40.90         |
| 7        | Fayetteville / Sandhills / Robeson        | 54.20        | 42.46         |
| 8        | South Central / Union / Anson             | 36.36        | 61.20         |
| 9        | Randolph / Fort Bragg / Moore             | 51.24        | 45.90         |
| 10       | Western Foothills / Nw Gaston / Cleveland | 35.38        | 62.47         |
| 11        | Asheville / Mountains / Buncombe          | 50.85        | 45.39         |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 52.15        | 45.89         |
| 13        | Triangle Suburbs / Johnston / Wayne      | 49.61        | 47.54          |
| 14        | Charlotte South / Ballantyne / Gaston    | 39.34        | 58.58          |
| Statewide| —                                         | 50.23        | 46.92         |

| Statewide Winner | Margin |
|------------------|--------|
| Perdue (D)       | +3.31  |

*In 2008, Beverly Perdue (D) won the North Carolina governorship by approximately 3.31 percentage points (50.23% to 46.92%). Then Charlotte Mayor Pat McCrory (R), the Republican nominee, would later become governor in 2013.*

---

## District-Level 2008 U.S. Senate Results

| District  | Region                                   | Hagan (D) % | Dole (R) % |
|-----------|------------------------------------------|-------------|------------|
| 1         | Northeast / Inner Coastal Plain           | 59.55       | 38.61      |
| 2         | Raleigh Metro / North Wake                | 55.69       | 41.32      |
| 3         | Eastern / Crystal Coast / Carteret        | 44.94       | 52.17      |
| 4         | Durham / Chapel Hill / RTP / Orange       | 65.45       | 31.89      |
| 5         | Northwest / Foothills / Wilkes            | 46.81       | 49.44      |
| 6         | Greensboro / Piedmont Triad / High Point  | 59.04       | 38.15      |
| 7         | Fayetteville / Sandhills / Robeson        | 53.53       | 43.04      |
| 8         | South Central / Union / Anson             | 41.58       | 54.63      |
| 9         | Randolph / Fort Bragg / Moore             | 52.11       | 44.73      |
| 10        | Western Foothills / Nw Gaston / Cleveland | 41.92       | 54.00      |
| 11        | Asheville / Mountains / Buncombe          | 50.02       | 46.13      |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 61.99       | 34.98      |
| 13        | Triangle Suburbs / Johnston / Wayne       | 51.13       | 45.99         |
| 14        | Charlotte South / Ballantyne / Gaston     | 52.55       | 44.19      |
| Statewide | —                                        | 52.61       | 44.23      |

| Statewide Winner | Margin |
|------------------|--------|
| Hagan (D)        | +8.38  |

*In 2008, State Senator Kay Hagan (D) defeated incumbent Elizabeth Dole (R) for the U.S. Senate by 8.38 percentage points (52.61% to 44.23%).*

> **County Flips & Lasts:** Many rural and suburban counties that had previously supported Republican Senate candidates voted Democratic in 2008, contributing to Hagan's victory. For several, this was the last time they supported a Democrat for U.S. Senate or any federal office, marking a high-water mark for Democrats in the state during the Obama wave.

---

## District-Level 2010 U.S. Senate Results

| District | Region                                   | Marshall (D) % | Burr (R) % |
|----------|------------------------------------------|----------------|------------|
| 1        | Northeast / Inner Coastal Plain           | 52.75          | 45.83      |
| 2        | Raleigh Metro / North Wake                | 47.78          | 49.71      |
| 3        | Eastern / Crystal Coast / Carteret        | 35.85          | 62.19      |
| 4        | Durham / Chapel Hill / RTP / Orange       | 59.89          | 38.06      |
| 5        | Northwest / Foothills / Wilkes            | 34.53          | 63.08      |
| 6        | Greensboro / Piedmont Triad / High Point  | 45.45          | 52.47      |
| 7        | Fayetteville / Sandhills / Robeson        | 41.35          | 56.69      |
| 8        | South Central / Union / Anson             | 31.79          | 65.95      |
| 9        | Randolph / Fort Bragg / Moore             | 42.93          | 54.92      |
| 10       | Western Foothills / Nw Gaston / Cleveland | 32.17          | 65.38      |
| 11        | Asheville / Mountains / Buncombe          | 41.17          | 56.04      |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 53.67          | 44.57      |
| 13        | Triangle Suburbs / Johnston / Wayne       | 42.79          | 55.22      |
| 14        | Charlotte South / Ballantyne / Gaston     | 41.68          | 56.22      |
| Statewide| —                                        | 43.04          | 54.82      |

| Statewide Winner | Margin |
|------------------|--------|
| Burr (R)         | +11.78 |

*In 2010, Senator Richard Burr (R) was re-elected, defeating Secretary of State Elaine Marshall (D) by 11.78 percentage points (54.82% to 43.04%).*

> **County Flips & Context:** The 2010 Senate race reflected the national Republican wave, with Burr expanding his margins in rural and suburban districts. Marshall performed best in urban and minority-heavy areas, but the GOP made gains nearly everywhere. This election marked a consolidation of Republican strength in North Carolina’s federal races.

---

## District-Level 2012 Presidential Results

| District | Region                                   | Obama % | Romney % |
|----------|------------------------------------------|---------|----------|
| 1        | Northeast / Inner Coastal Plain           | 54.10   | 45.10    |
| 2        | Raleigh Metro / North Wake                | 58.20   | 40.60    |
| 3        | Eastern / Crystal Coast / Carteret        | 38.50   | 60.20    |
| 4        | Durham / Chapel Hill / RTP / Orange       | 66.00   | 32.60    |
| 5        | Northwest / Foothills / Wilkes            | 38.00   | 60.60    |
| 6        | Greensboro / Piedmont Triad / High Point  | 56.10   | 42.60    |
| 7        | Fayetteville / Sandhills / Robeson        | 48.00   | 50.60    |
| 8        | South Central / Union / Anson             | 33.00   | 65.40    |
| 9        | Randolph / Fort Bragg / Moore             | 46.00   | 52.20    |
| 10       | Western Foothills / Nw Gaston / Cleveland | 31.00   | 67.00    |
| 11        | Asheville / Mountains / Buncombe          | 44.00   | 54.00    |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 62.00   | 36.00    |
| 13        | Triangle Suburbs / Johnston / Wayne       | 48.50   | 50.00    |
| 14        | Charlotte South / Ballantyne / Gaston     | 54.00   | 44.00    |
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
| 3        | Eastern / Crystal Coast / Carteret        | 38.00        | 60.00         |
| 4        | Durham / Chapel Hill / RTP / Orange       | 62.00        | 36.00         |
| 5        | Northwest / Foothills / Wilkes            | 38.00        | 60.00         |
| 6        | Greensboro / Piedmont Triad / High Point  | 52.00        | 46.00         |
| 7        | Fayetteville / Sandhills / Robeson        | 46.00        | 52.00         |
| 8        | South Central / Union / Anson             | 32.00        | 66.00         |
| 9        | Randolph / Fort Bragg / Moore             | 44.00        | 54.00         |
| 10       | Western Foothills / Nw Gaston / Cleveland | 30.00        | 68.00         |
| 11        | Asheville / Mountains / Buncombe          | 42.00        | 56.00         |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 54.00        | 44.00         |
| 13        | Triangle Suburbs / Johnston / Wayne       | 46.00        | 52.00         |
| 14        | Charlotte South / Ballantyne / Gaston     | 48.00        | 50.00         |
| Statewide | —                                        | 43.16        | 54.96         |

| Statewide Winner | Margin |
|------------------|--------|
| McCrory (R)      | +11.80 |

*In 2012, Pat McCrory (R) won the governorship, defeating Walter Dalton (D) by 11.8 percentage points (54.96% to 43.16%).*

> **County Flips & Lasts:** McCrory flipped a large number of rural and suburban counties that had supported Democrats for governor in 2008, including Robeson, Columbus, and Richmond. For many of these, 2012 was the last time they were even close for Democrats in a statewide race. The realignment in these counties foreshadowed the GOP’s dominance in subsequent cycles and the end of the Democratic “blue wall” in eastern North Carolina.

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

---

## District-Level 2016 Presidential Results

| District | Region                                   | Clinton % | Trump % |
|----------|------------------------------------------|-----------|---------|
| 1        | Northeast / Inner Coastal Plain           | 53.63     | 43.78   |
| 2        | Raleigh Metro / North Wake                | 58.21     | 36.22   |
| 3        | Eastern / Crystal Coast / Carteret        | 35.34     | 61.41   |
| 4        | Durham / Chapel Hill / RTP / Orange       | 64.98     | 30.99   |
| 5        | Northwest / Foothills / Wilkes            | 36.68     | 59.15   |
| 6        | Greensboro / Piedmont Triad / High Point  | 53.36     | 42.92   |
| 7        | Fayetteville / Sandhills / Robeson        | 41.73     | 54.64   |
| 4        | Durham / Chapel Hill / RTP / Orange       | 63.56        | 33.77         |
| 5        | Northwest / Foothills / Wilkes            | 35.86        | 60.34         |
| 6        | Greensboro / Piedmont Triad / High Point  | 52.13        | 44.74         |
| 7        | Fayetteville / Sandhills / Robeson        | 41.32        | 54.89         |
| 8        | South Central / Union / Anson             | 29.67        | 66.02         |
| 9        | Randolph / Fort Bragg / Moore             | 43.63        | 52.83         |
| 10       | Western Foothills / Nw Gaston / Cleveland | 28.53        | 66.77         |
| 11        | Asheville / Mountains / Buncombe          | 41.68        | 54.17         |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 58.61        | 37.45      |
| 13        | Triangle Suburbs / Johnston / Wayne       | 45.88        | 50.89         |
| 14        | Charlotte South / Ballantyne / Gaston     | 49.07        | 47.00         |
| Statewide | —                                        | 47.45        | 49.02         |

| Statewide Winner | Margin |
|------------------|--------|
| Cooper (D)       | +0.57  |

*In 2016, Roy Cooper (D) narrowly won the North Carolina governorship, defeating incumbent Pat McCrory (R) by approximately 0.57 percentage points (47.45% to 46.88%).*

> **County Flips & Lasts:** Cooper performed well in urban and suburban areas, maintaining Democratic strongholds. However, he also flipped some rural counties that had supported Trump in the presidential election, indicating a potential backlash against McCrory's policies—especially the controversial House Bill 2 (HB2, the "bathroom bill")—and his unpopularity. The election results further illustrated the complex and shifting political landscape in North Carolina, with significant variations at the county level.

---

## District-Level 2016 U.S. Senate Results

| District  | Region                                   | Ross (D) % | Burr (R) % |
|-----------|------------------------------------------|-------------|------------|
| 1         | Northeast / Inner Coastal Plain           | 53.10       | 44.57      |
| 2         | Raleigh Metro / North Wake                | 55.89       | 41.01      |
| 3         | Eastern / Crystal Coast / Carteret        | 34.91       | 61.53      |
| 4         | Durham / Chapel Hill / RTP / Orange       | 63.56       | 33.77      |
| 5         | Northwest / Foothills / Wilkes            | 35.86       | 60.34      |
| 6         | Greensboro / Piedmont Triad / High Point  | 52.13       | 44.74      |
| 7         | Fayetteville / Sandhills / Robeson        | 41.32       | 54.89         |
| 8         | South Central / Union / Anson             | 29.67        | 66.02         |
| 9         | Randolph / Fort Bragg / Moore             | 43.63        | 52.83      |
| 10        | Western Foothills / Nw Gaston / Cleveland | 28.53        | 66.77         |
| 11        | Asheville / Mountains / Buncombe          | 41.68        | 54.17         |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 58.61        | 37.45      |
| 13        | Triangle Suburbs / Johnston / Wayne       | 45.88        | 50.89         |
| 14        | Charlotte South / Ballantyne / Gaston     | 49.07        | 47.00         |
| Statewide | —                                        | 45.36       | 51.06      |

| Statewide Winner | Margin |
|------------------|--------|
| Burr (R)         | +5.70  |

*In 2016, Senator Richard Burr (R) was re-elected, defeating challenger and future congresswoman Deborah Ross (D) by approximately 5.70 percentage points (51.06% to 45.36%).*

> **County Flips & Context:** Burr performed strongly in rural and some suburban counties, consolidating Republican gains from previous elections. However, his support dipped in urban areas and some traditionally Democratic strongholds. The election results reflected a continuation of the partisan realignment in North Carolina, with Burr benefiting from high Republican turnout and support from white working-class voters.

---

## District-Level 2020 Presidential Results

| District | Region                                   | Biden (D) % | Trump (R) % |
|----------|------------------------------------------|-------------|-------------|
| 1        | Northeast / Inner Coastal Plain           | 53.11       | 45.82       |
| 2        | Raleigh Metro / North Wake                | 63.37       | 34.72       |
| 3        | Eastern / Crystal Coast / Carteret        | 36.59       | 61.91       |
| 4        | Durham / Chapel Hill / RTP / Orange       | 66.77       | 31.78       |
| 5        | Northwest / Foothills / Wilkes            | 38.69       | 59.94       |
| 6        | Greensboro / Piedmont Triad / High Point  | 55.50       | 43.12       |
| 7        | Fayetteville / Sandhills / Robeson        | 42.97       | 55.69       |
| 8        | South Central / Union / Anson             | 32.34       | 66.35       |
| 9        | Randolph / Fort Bragg / Moore             | 45.27       | 53.23       |
| 10       | Western Foothills / Nw Gaston / Cleveland | 29.65       | 69.11       |
| 11        | Asheville / Mountains / Buncombe          | 44.15       | 54.28       |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 64.24       | 34.14       |
| 13        | Triangle Suburbs / Johnston / Wayne       | 49.97       | 48.28       |
| 14        | Charlotte South / Ballantyne / Gaston     | 57.33       | 40.97       |
| Statewide | —                                        | 48.58       | 49.94       |

| Statewide Winner | Margin |
|------------------|--------|
| Trump (R)        | +1.36  |

*In 2020, Donald Trump (R) narrowly won North Carolina over Joe Biden (D) by approximately 1.36 percentage points (49.94% to 48.58%).*

> **County Flips & Lasts:** Scotland County, which had previously voted Democratic, flipped to Trump in 2020, reflecting the continued Republican gains in rural and working-class areas of eastern North Carolina. Robeson County, home to the Lumbee tribe, remained Republican after flipping in 2016. Several Obama-Trump counties in the district, such as Robeson and Bladen, voted for Trump by even larger margins in 2020 than in 2016, underscoring the deepening realignment and growing Republican strength in these rural areas. The district overall saw a further narrowing of the Democratic margin, with Biden carrying NC-01 by just over 7 points, down from previous cycles. Urban and Black-majority precincts remained Democratic, but rural counties trended further Republican, continuing the realignment seen throughout the decade.

---

## District-Level 2020 Gubernatorial Results

| District | Region                                   | Cooper (D) % | Forest (R) % |
|----------|------------------------------------------|--------------|--------------|
| 1        | Northeast / Inner Coastal Plain           | 55.83        | 43.15        |
| 2        | Raleigh Metro / North Wake                | 66.24        | 32.19        |
| 3        | Eastern / Crystal Coast / Carteret        | 39.09        | 59.37        |
| 4        | Durham / Chapel Hill / RTP / Orange       | 69.15        | 29.59        |
| 5        | Northwest / Foothills / Wilkes            | 42.67        | 56.00        |
| 6        | Greensboro / Piedmont Triad / High Point  | 58.68        | 39.81        |
| 7        | Fayetteville / Sandhills / Robeson        | 46.73        | 51.79        |
| 8        | South Central / Union / Anson             | 35.67        | 63.00         |
| 9        | Randolph / Fort Bragg / Moore             | 48.87        | 49.51        |
| 10       | Western Foothills / Nw Gaston / Cleveland | 32.90        | 65.76        |
| 11        | Asheville / Mountains / Buncombe          | 47.21        | 51.21        |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 65.87        | 32.21        |
| 13        | Triangle Suburbs / Johnston / Wayne       | 53.19        | 45.27        |
| 14        | Charlotte South / Ballantyne / Gaston     | 58.73        | 39.56        |
| Statewide| —                                        | 51.51        | 47.01        |

| Statewide Winner | Margin |
|------------------|--------|
| Cooper (D)       | +4.50  |

*In 2020, Governor Roy Cooper (D) was re-elected, defeating term limited Lt. Governor Dan Forest (R) by approximately 4.50 percentage points (51.51% to 47.01%).*

> **County Flips & Context:** Cooper performed strongly in urban and suburban districts, as well as in the northeast, but some rural and working-class counties continued to trend Republican. Robeson and Scotland counties, which had previously supported Democratic gubernatorial candidates, remained Republican in 2020, reflecting the ongoing realignment in eastern North Carolina. The results highlight the persistence of split-ticket voting in some areas, with Cooper outperforming Biden and other Democrats in several rural and exurban districts.

---

## District-Level 2020 Attorney General Results

| District | Region                                   | Stein (D) % | O'Neill (R) % |
|----------|------------------------------------------|-------------|---------------|
| 1        | Northeast / Inner Coastal Plain           | 55.62       | 44.38         |
| 2        | Raleigh Metro / North Wake                | 64.18       | 35.82         |
| 3        | Eastern / Crystal Coast / Carteret        | 38.20       | 61.80         |
| 4        | Durham / Chapel Hill / RTP / Orange       | 68.04       | 31.96         |
| 5        | Northwest / Foothills / Wilkes            | 39.98       | 60.02         |
| 6        | Greensboro / Piedmont Triad / High Point  | 56.82       | 43.18         |
| 7        | Fayetteville / Sandhills / Robeson        | 45.33       | 54.67         |
| 8        | South Central / Union / Anson             | 34.39       | 65.61         |
| 9        | Randolph / Fort Bragg / Moore             | 47.29       | 52.71         |
| 10       | Western Foothills / Nw Gaston / Cleveland | 32.01       | 67.99         |
| 11        | Asheville / Mountains / Buncombe          | 45.64       | 54.36         |
| 12        | Charlotte Urban / Uptown / Mecklenburg    | 65.09       | 34.91         |
| 13        | Triangle Suburbs / Johnston / Wayne       | 51.75       | 48.25         |
| 14        | Charlotte South / Ballantyne / Gaston     | 56.94       | 43.06         |
| Statewide| —                                        | 50.12       | 49.88         |

| Statewide Winner | Margin |
|------------------|--------|
| Stein (D)        | +0.24  |

*In 2020, Attorney General Josh Stein (D) was narrowly re-elected, defeating Jim O'Neill (R) by just 0.24 percentage points (50.12% to 49.88%).*

> **County Flips & Context:** Stein performed strongly in urban and suburban districts, but many rural and working-class counties continued to trend Republican. Robeson and Scotland counties, which had previously supported Democratic AG candidates, remained Republican in 2020. The razor-thin margin highlights the competitiveness of statewide races in North Carolina and the persistence of split-ticket voting, as Stein outperformed Biden and other Democrats in several key districts. Notably, 2020 also saw Senator Thom Tillis (R) narrowly re-elected statewide, further illustrating the complex and competitive nature of North Carolina’s electorate and the challenges for Democrats in converting close statewide races into victories. Jim O'Neill, the Republican nominee, is the Forsyth County District Attorney; Forsyth is home to Winston-Salem, a major urban center in the Piedmont Triad region. After this race, Stein ran for governor in 2024 to succeed Roy Cooper, who was term-limited.

---

## District-Level 2024 Presidential Results

| District | Dem %  | Rep %  |
|----------|--------|--------|
| 1        | 51.06  | 48.05  |
| 2        | 63.08  | 35.26  |
| 3        | 34.76  | 64.37  |
| 4        | 66.39  | 32.24  |
| 5        | 38.16  | 60.82  |
| 6        | 54.59  | 44.13  |
| 7        | 41.55  | 57.57  |
| 8        | 31.90  | 67.14  |
| 9        | 43.89  | 55.07  |
| 10       | 29.43  | 69.74  |
| 11        | 45.00  | 53.78  |
| 12       | 63.62  | 34.65  |
| 13       | 49.76  | 48.80  |
| 14       | 57.00  | 41.64  |
| Statewide| 47.81  | 51.01  |

| Statewide Winner | Margin |
|------------------|--------|
| Trump (R)        | +3.20  |

*In 2024, Donald Trump (R) won North Carolina over Kamala Harris (D) by approximately 3.20 percentage points (51.01% to 47.81%).*

> **County Flips & Context:** In 2024, Anson and Pasquotank counties flipped to Trump for the first time, while Nash County, a perennial swing and bellwether, flipped back to Trump after supporting Biden in 2020. These shifts highlight the continued Republican gains in rural and eastern North Carolina, as well as the volatility of key swing counties. Demographic changes, turnout patterns, and candidate dynamics all contributed to these notable flips and the overall statewide result.

---

## District-Level 2024 Gubernatorial Results

| District | Stein (D) %  | Robinson (R) %  |
|----------|--------|--------|
| 1        | 56.53  | 40.03  |
| 2        | 71.09  | 23.48  |
| 3        | 41.33  | 53.53  |
| 4        | 71.89  | 24.31  |
| 5        | 46.32  | 48.59  |
| 6        | 61.67  | 33.48  |
| 7        | 50.14  | 44.22  |
| 8        | 39.28  | 55.22  |
| 9        | 50.53  | 44.26  |
| 10       | 37.00  | 57.65  |
| 11        | 51.86  | 43.60  |
| 12       | 68.95  | 25.98  |
| 13       | 57.57  | 36.80  |
| 14       | 64.44  | 30.03  |
| Statewide| 54.90  | 40.08  |

| Statewide Winner | Margin |
|------------------|--------|
| Stein (D)     | +14.82 |

*In 2024, Attorney General Josh Stein (D) defeated Lieutenant Governor Mark Robinson (R) for the open governorship by approximately 14.82 percentage points (54.90% to 40.08%). Stein, a moderate Democrat from Wake County, benefited from strong support in urban and suburban districts, especially in the Triangle and Charlotte regions. Robinson, a polarizing conservative and the state's first Black Lieutenant Governor, performed best in rural and exurban areas but underperformed compared to the GOP's presidential ticket. The result highlights the persistence of split-ticket voting in North Carolina, as voters chose a Republican for president but a Democrat for governor. No major county flips were recorded, but Stein's large margins in Wake and Mecklenburg counties underscore the state's ongoing urban/suburban realignment. Third-party and independent candidates received a notable share, especially in competitive and urban districts. The 2024 race was shaped by demographic trends, candidate backgrounds, and turnout patterns, with Stein's appeal to moderates and minority voters proving decisive.*

> **County Flips & Split-Ticket Context:** While no major counties flipped parties in the 2024 gubernatorial race, several counties that voted for Trump at the presidential level also supported Stein for governor, demonstrating persistent split-ticket voting. Notably, counties such as Alamance, Cabarrus, Franklin, Brunswick, Lee, Transylvania, Henderson, and Jackson backed Trump for president but Stein for governor. This pattern underscores Stein's crossover appeal, especially among moderate suburban and coastal voters, and highlights the unique dynamics of North Carolina's statewide elections, where candidate quality and local issues can drive significant ticket-splitting even in an era of increasing polarization.

---

## District-Level 2024 Supreme Court Results

| District  | Dem %  | Rep %  |
|-----------|--------|--------|
| 1         | 53.24  | 46.76  |
| 2         | 64.94  | 35.06  |
| 3         | 37.07  | 62.93  |
| 4         | 68.35  | 31.65  |
| 5         | 40.18  | 59.82  |
| 6         | 56.71  | 43.29  |
| 7         | 43.98  | 56.02  |
| 8         | 34.21  | 65.79  |
| 9         | 46.07  | 53.93  |
| 10        | 31.92  | 68.08  |
| 11        | 47.00  | 53.00  |
| 12        | 65.95  | 34.05  |
| 13       | 52.04  | 47.96  |
| 14       | 58.86  | 41.14  |
| Statewide | 50.02  | 49.98  |

*Note: The 2024 State Supreme Court race between Allison Riggs (D) and Jefferson Griffin (R) was in litigation until May 7, 2025, due to the small final statewide margin. Riggs ultimately won by just 734 votes, preventing a 6-1 Republican supermajority on the court.*

> **Context:** The Supreme Court race in 2024 was highly contentious and closely watched, with significant implications for the court's partisan balance. The litigation following the election highlighted the ongoing partisan divisions and the stakes involved in North Carolina's judicial races. The eventual ruling and its impact on the court's composition will be critical in shaping the state's legal and political landscape in the coming years.

---

## District-Level 2024 Lieutenant Governor Results

| District | Hunt (D) % | Weatherman (R) % | Oth % |
|----------|------------|------------------|-------|
| 1        | 53.03      | 44.57            | 2.40  |
| 2        | 64.34      | 33.01            | 2.65  |
| 3        | 36.72      | 59.97            | 3.31  |
| 4        | 67.76      | 29.83            | 2.41  |
| 5        | 39.68      | 57.47            | 2.85  |
| 6        | 56.26      | 40.76            | 2.97  |
| 7        | 44.03      | 53.09            | 2.88  |
| 8        | 33.81      | 63.31            | 2.88  |
| 9        | 45.37      | 51.46            | 3.17  |
| 10       | 31.42      | 65.86            | 2.72  |
| 11        | 46.36      | 50.85            | 2.79  |
| 12       | 65.28      | 31.85            | 2.87  |
| 13       | 51.55      | 45.35            | 3.10  |
| 14       | 58.28      | 39.05            | 2.68  |
| Statewide| 49.54      | 47.63            | 2.83  |

| Statewide Winner | Margin |
|------------------|--------|
| Hunt (D)         | +1.91  |

*In 2024, State Senator Rachel Hunt (D), daughter of former Governor Jim Hunt, narrowly defeated Republican Hal Weatherman for Lieutenant Governor by 1.91 percentage points (49.54% to 47.63%). Hunt's win is notable as it marks a Democratic flip of the office, likely aided by Josh Stein's strong performance at the top of the ticket and her own high profile as a moderate legislator and political legacy. Weatherman, a conservative businessman and former chief of staff to Lt. Gov. Dan Forest, performed well in rural and exurban areas, but Hunt's margins in urban and suburban districts, especially in the Triangle and Charlotte, proved decisive. Third-party and independent candidates received a small but notable share, especially in competitive districts.*

> **Context & Coattails:** Hunt's victory is widely attributed to the coattail effect of Stein's landslide win for governor, as well as her own appeal as a moderate and the daughter of a popular former governor. The result demonstrates the potential for Democratic gains in statewide down-ballot races when the top of the ticket is strong, and highlights the importance of candidate quality and political legacy in North Carolina politics. This race also underscores the ongoing volatility and competitiveness of the state's political landscape, with split-ticket voting and local dynamics playing a key role in the outcome.

---

## Methodology & AI Assistance Disclosure
This case study was researched, analyzed, and written by the author, with the assistance of GitHub Copilot (AI) for code automation, data extraction, and some markdown editing. All substantive analysis, narrative, and editorial decisions reflect the author's own work, insights, and pattern recognition. AI was used as a tool to streamline technical tasks, not to generate conclusions or interpretations.

**Estimated Contribution:** Approximately 85% of this project—including all data sourcing, analysis, interpretation, and conclusions—is original work by the author. GitHub Copilot (AI) contributed about 15%, primarily by automating repetitive coding, assisting with data extraction, and providing technical formatting support. All AI usage was supervised, reviewed, and directed by the author to ensure accuracy, transparency, and responsible use.

---

## Analysis Notes
- Districts with major partisan shifts will be highlighted in the narrative.
- Split-ticket voting and outlier districts will be discussed.
- Visualizations (maps, charts) may be added for clarity.
- Cabarrus and Alamance counties, while still leaning Republican, have become more competitive in recent cycles (2020 margin: Cabarrus R+9.4, Alamance R+7.1; 2024 margin: Cabarrus R+7.7, Alamance R+4.9) as unaffiliated registration has surpassed both major parties and suburban growth accelerates due to proximity to Charlotte, the Triad, and the Triangle.
    - In 2020, Trump carried Cabarrus County 53.94% to 44.50%, but it was also the first time since 2008 that a Democrat cracked 40% there, signaling increased competitiveness.
    - In 2020, Trump carried Alamance County 53.50% to 45.10%, marking the first time since 2008 that a Democrat cracked 45% in the county (Obama received 44.94% that year).
    - In 2024, Trump carried Cabarrus County 53.03% to 45.34% (R+7.7), continuing the trend of narrowing margins.
    - In 2024, Trump carried Alamance County 53.36% to 45.22% (R+8.1) Again, Democrats maintained their improved share from 2020.
    - Notably, the Democratic share in Alamance County was nearly identical in both 2020 (45.10%) and 2024 (45.22%), a pattern recognized by the analyst. This statistical similarity across cycles highlights the value of close data examination and underscores the importance of tracking subtle but persistent trends in competitive counties.
    - The influx of new industries and residents has also contributed to rising voter registration and turnout in both counties, with unaffiliated voters now outnumbering both Democrats and Republicans. In recent statewide elections, shifts in Cabarrus and Alamance have been pivotal to overall margins, underscoring their growing importance in North Carolina's political landscape. These trends mirror broader national patterns of suburban realignment and the transformation of formerly safe Republican counties into competitive battlegrounds.
    - In Cabarrus County, fast-growing communities include Concord, Kannapolis, and Harrisburg, each seeing significant residential and commercial development. In Alamance County, Graham, Burlington, and Mebane are expanding rapidly, with Mebane in particular attracting new industry and commuters due to its location along the I-40/I-85 corridor. Notably, a Buc-ee’s is scheduled to open in Mebane in late 2026 or early 2027, highlighting the area’s commercial growth and rising regional profile. These cities and towns exemplify the suburban growth and demographic change driving the region's political transformation.

---

## References
- [NC State Board of Elections](https://www.ncsbe.gov/)
- [Dave's Redistricting App](https://davesredistricting.org/)

---

*This file will be updated as new datasets or analysis are added.*

## Trends in NC-01 (Northeast / Inner Coastal Plain)

**Summary:**  
NC-01 has historically leaned Democratic in presidential, gubernatorial, and Senate races, but the Democratic margin has steadily narrowed from 2008 through 2024. The district’s Democratic strength is rooted in its significant Black population and rural communities, but Republican gains have accelerated in recent cycles, especially in rural and working-class counties.

**Key Trends:**
- **Presidential:** Democratic candidates (Obama, Clinton, Biden, Harris) all carried NC-01, but the margin dropped from 56.4% (2008) to 53.6% (2016) and just 3 (51-48) points in 2024, reflecting a slow but steady Republican advance.
- **Gubernatorial:** Democratic candidates (Perdue, Cooper) have won the district, but with shrinking margins, mirroring national and statewide trends.
- **Senate:** Democratic Senate candidates (Hagan, Ross) have performed well, but again with reduced margins compared to earlier cycles.
- **County Flips:** Several counties in NC-01 (e.g., Gates, Martin) have flipped from Democratic to Republican in at least one major race since 2012, signaling realignment in rural eastern NC.
- **Demographics:** The district is home to a large Black population, but that is gradually decreasing due to the black belt counties coontinuously depopulating, historically supported Democrats but has shown signs of shifting, especially among rural voters.
- **Suburban Realignment:** Cabarrus and Alamance counties, while still Republican-leaning, now have more registered unaffiliated voters than either Democrats or Republicans. Both are becoming increasingly suburban as bedroom communities for Charlotte, the Piedmont Triad, and the Research Triangle, contributing to changing political dynamics and greater competitiveness.
- **Realignment:** The district exemplifies the broader trend of rural and working-class voters moving toward the GOP, even as urban and Black-majority precincts remain Democratic. Split-ticket voting has declined, and the district is now more competitive than a decade ago.

**Narrative Note:**  
> *NC-01’s evolution reflects the national realignment of rural and minority-heavy districts. While still Democratic-leaning, the district’s margin has eroded as Republicans make inroads with rural, working-class, and Native voters. The Lumbee tribe’s shifting allegiances in Robeson County are especially notable in NC-07's stronger republican lean through the years. NC-01 remains a bellwether for the future of Democratic strength in rural eastern North Carolina, as shown by Harris’s narrow 3-point win in 2024.*
