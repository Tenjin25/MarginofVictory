# MarginofVictory v2.0 - Enhanced Political Margin of Victory Calculator

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Sample Output](#sample-output)
- [Real-World Case Studies](#real-world-case-studies)
- [Installation and Usage](#installation-and-usage)
- [Version History](#version-history)
- [Citations and References](#citations-and-references)

---

## Project Overview

**MOVCalculator** is a Java application designed to analyze electoral race competitiveness by calculating the margin of victory and providing professional race ratings. This enhanced version (v2.0) demonstrates programming skills applied to real-world political analysis, following industry standards and CPT-236 course objectives.

**Developer:** Shamar Davis  
**Course:** CPT-236 (Computer Programming)  
**Version:** 2.0 (Enhanced)  
**Date:** July 7, 2025

---

## Features

- **Margin of Victory Calculation:** Computes the absolute difference between candidate vote percentages.
- **Professional Race Rating System:** Classifies races as Tossup, Tilt, Lean, Likely, or Safe using industry-standard thresholds.
- **Comprehensive Input Validation:** Ensures all vote percentages are between 0 and 100, with clear error messages.
- **Winner Determination:** Identifies the leading candidate and party affiliation.
- **Flip Detection:** Signals a "FLIP" if the winner's party differs from the incumbent party.
- **Professional Output:** Displays results in a clear, formatted summary suitable for academic and real-world use.
- **Robust Error Handling:** Guides users to correct invalid or out-of-range input.

---

## Sample Output

```
State Abbreviation: NC
District Number: 7
Enter the first candidate's name: Jane Smith
Enter the second candidate's name: John Doe
What is the party affiliation of Jane Smith? Democratic
Jane Smith is a Democratic.
What is the party affiliation of John Doe? Republican
John Doe is a Republican.
Which party has the incumbency? Republican
Enter the vote percentage for Jane Smith (0-100): 52.8
Enter the vote percentage for John Doe (0-100): 47.2

--- Election Results ---
State: NC | District: 7
Jane Smith (Democratic): 52.80%
John Doe (Republican): 47.20%
Margin of Victory: 5.60%
Jane Smith (Democratic) is the winner. Race rating: Lean Democratic
** FLIP: Democratic gains this seat! **
```

---

## Real-World Case Studies

These examples demonstrate how the MOVCalculator's race rating system applies to actual election outcomes:

### Ultra-Close Races (Tossup Category)

- **North Carolina Supreme Court (2024):**  
  Decided by exactly 734 votes—a margin of roughly 0.01% in a statewide race with millions of voters. Allison Riggs (D) won, but the race remained in litigation until May 7, 2025, demonstrating how ultra-close margins can trigger extended legal challenges.

- **Pennsylvania U.S. Senate (2024):**  
  Dave McCormick (R) defeated incumbent Bob Casey Jr. (D) by approximately 16,000 votes out of nearly 7 million cast—a margin of roughly 0.2%. Casey challenged the results in court until the week of Thanksgiving 2024, showing how even federal races can trigger extended legal battles when margins fall into the Tossup category.

- **Iowa's 2nd Congressional District (2020):**  
  Initially decided by just 6 votes, later certified with a 6-vote margin after multiple recounts.

### Tilt Category Examples

- **Nevada U.S. Senate (2022):**  
  Catherine Cortez Masto (D) defeated Adam Laxalt (R) by 7,928 votes, a margin of 0.78%—demonstrating a "Tilt" category race where the incumbent narrowly survived in a crucial swing state contest that helped determine Senate control.

- **Florida Governor (2018):**  
  Ron DeSantis (R) defeated Andrew Gillum (D) by just 32,463 votes out of over 8.2 million cast—a margin of 0.4%. This race occurred before the COVID-era political realignment that has since made Florida more reliably Republican.

### Lean Category Examples

- **Pennsylvania's 8th Congressional District (2024):**  
  Rob Bresnahan Jr. (R) defeated incumbent Matt Cartwright (D) by approximately 1.6%—demonstrating a "Lean" category race where the challenger successfully unseated an incumbent, flipping the seat from Democratic to Republican control in a closely divided district. Trump carried this district by approximately 8.49%, showing significant ticket-splitting where many Trump voters chose the Democratic incumbent.

- **California's 45th Congressional District (2024):**  
  Derek Tran (D) defeated incumbent Michelle Steel (R) by approximately 1.8%—another "Lean" category race showing how competitive districts can flip between parties when margins fall in this range. Harris carried this district by approximately 1.2%, demonstrating split-ticket voting where voters chose the presidential candidate from one party while selecting a House candidate from the opposing party.

### Split-Ticket Voting Analysis

- **Pennsylvania 8th (Trump +8.49%, Bresnahan (R) +1.6%):**  
  This district shows significant ticket-splitting favoring Democrats, where Trump's overwhelming performance (+8.49%) did not translate into an equally strong showing for the Republican House candidate. This represents a 6.89% ticket-split, indicating substantial crossover voting where Trump supporters chose the Democratic incumbent Cartwright.

- **California 45th (Harris +1.6%, Tran (D) +1.8%):**  
  This district shows modest ticket-splitting favoring Democrats, where the Democratic House candidate slightly outperformed Harris. This suggests effective campaigning by Tran and potential dissatisfaction with the Republican incumbent Steel, even in a district that narrowly preferred Harris for president.

**Strategic Implications:**  
Both districts demonstrate how the MOVCalculator's "Lean" classification correctly identifies seats where split-ticket voting can determine outcomes, making them genuine pickup opportunities despite modest presidential leans.

### Pennsylvania Electoral History and Regional Realignment

The MOVCalculator's rating system captures important electoral trends in Pennsylvania's suburban districts, particularly PA-07 and PA-08, which have experienced significant political realignment over the past decade:

#### Pennsylvania's 7th Congressional District Evolution

- **2024 Senate Results:**  
  Dave McCormick (R): 49.6%  
  Bob Casey Jr. (D): 47.8%  
  Margin: McCormick +1.8% (Lean Republican) ✅ CORRECTED CLASSIFICATION

- **2024 Presidential Results (Northampton County - Major PA-07 Component):**  
  Donald Trump (R): 50.40%  
  Kamala Harris (D): 48.62%  
  Margin: Trump +1.78% (Lean Republican)

- **Northampton County Electoral Volatility (2016-2024):**  
  - 2016: Trump +3.78% (Lean Republican) - First Republican victory since George H.W. Bush (1988)  
  - 2020: Biden +0.72% (Tilt Democratic) - Democratic recapture  
  - 2024: Trump +1.78% (Lean Republican) - Republican re-flip

- **2018 Senate Results:**  
  Bob Casey Jr. (D): 55.1%  
  Lou Barletta (R): 44.9%  
  Margin: Casey +10.2% (Safe Democratic)

**Electoral Shift:**  
PA-07 moved from Safe Democratic (+10.2%) to Lean Republican (+1.8%), representing a 12.0% swing toward Republicans between 2018 and 2024.

#### Pennsylvania's 8th Congressional District Evolution (Scranton/Wilkes-Barre Area)

- **2024 House Results:**  
  Rob Bresnahan Jr. (R): 50.8%  
  Matt Cartwright (D): 49.2%  
  Margin: Bresnahan +1.6% (Lean Republican)  
  Incumbent Defeated: Cartwright loses after three consecutive victories

- **2024 Senate Results:**  
  Dave McCormick (R): 52.25%  
  Bob Casey Jr. (D): 47.75%  
  Margin: McCormick +4.5% (Lean Republican)

- **2024 Presidential Results (District Overall):**  
  Donald Trump (R): ~54.25%  
  Kamala Harris (D): ~45.75%  
  Margin: Trump +8.5% (Likely Republican) - Populist Democratic crossover effect

- **Historical House Results - Cartwright Performance Trajectory:**  
  - 2022: Cartwright (D) +2.4% (Lean Democratic)  
  - 2020: Cartwright (D) +3.8% (Lean Democratic)  
  - 2018: Cartwright (D) +9.8% (Likely Democratic)

- **2018 Senate Results (Historical Context):**  
  Bob Casey Jr. (D): 53.1%  
  Lou Barletta (R): 46.9%  
  Margin: Casey +6.2% (Likely Democratic)

---

## Installation and Usage

1. **Clone or Download** this repository.
2. **Compile** the program:
   ```
   javac MarginOfVictory.java
   ```
3. **Run** the program:
   ```
   java MarginOfVictory
   ```
4. **Follow the prompts** to enter state, district, candidate names, party affiliations, incumbent party, and vote percentages.

---

## Version History

- **v1.0:** Prototype with basic margin calculation and output.
- **v2.0:** Enhanced with professional output, robust input validation, race rating, and flip detection.

---

## Citations and References

- Industry-standard race rating thresholds: [Cook Political Report](https://www.cookpolitical.com/)
- Real-world election data: [Ballotpedia](https://ballotpedia.org/)
- Java documentation: [Oracle Java SE Docs](https://docs.oracle.com/en/java/)

---

**Copyright (c) 2025 Shamar Davis.  
For academic and professional use in CPT-236 and portfolio demonstration.**
