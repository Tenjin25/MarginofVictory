/**
 * MOVCalculator v3.0+ Pennsylvania Electoral Analysis Enhancement
 * Demonstrates corrected historical data integration and volatility assessment
 * 
 * Educational Objective: Advanced temporal programming with data accuracy validation
 * and multi-district comparative analysis for professional political applications
 * 
 * @author Shamar Davis
 * @course CPT-236 (Computer Programming)
 * @version 3.0 (Corrected Historical Analysis)
 */
public class PennsylvaniaElectoralAnalyzer {
    
    // PA-07 Northampton County volatility data - demonstrates swing territory programming
    private static final double NORTHAMPTON_2016_TRUMP_MARGIN = 3.78;     // Lean Republican
    private static final double NORTHAMPTON_2020_BIDEN_MARGIN = 0.72;     // Tilt Democratic  
    private static final double NORTHAMPTON_2024_TRUMP_MARGIN = 1.78;     // Lean Republican
    
    // PA-08 Cartwright decline data - corrected 2022 margin
    private static final double CARTWRIGHT_2018_MARGIN = 9.8;             // Likely Democratic
    private static final double CARTWRIGHT_2020_MARGIN = 3.8;             // Lean Democratic  
    private static final double CARTWRIGHT_2022_MARGIN = 2.4;             // Lean Democratic (CORRECTED)
    private static final double BRESNAHAN_2024_MARGIN = 1.6;              // Lean Republican
    
    // Professional formatting for electoral analysis
    private static final DecimalFormat MARGIN_FORMAT = new DecimalFormat("0.00");
    private static final DecimalFormat SWING_FORMAT = new DecimalFormat("0.0");
    
    /**
     * Comprehensive Pennsylvania competitive district analysis
     * Integrates both corrected historical data and electoral volatility patterns
     * 
     * Educational Value: Demonstrates complex multi-district programming
     * requiring temporal analysis and comparative assessment
     */
    public static void analyzePennsylvaniaCompetitiveDistricts() {
        System.out.println("PENNSYLVANIA COMPETITIVE DISTRICTS ANALYSIS - CORRECTED DATA");
        System.out.println("═══════════════════════════════════════════════════════════════════════");
        System.out.println();
        
        // PA-07 Northampton County volatility analysis
        System.out.println("PA-07 NORTHAMPTON COUNTY ELECTORAL VOLATILITY:");
        System.out.println("2016: Trump +" + MARGIN_FORMAT.format(NORTHAMPTON_2016_TRUMP_MARGIN) + 
                          "% (Lean Republican) - 28-year breakthrough");
        System.out.println("2020: Biden +" + MARGIN_FORMAT.format(NORTHAMPTON_2020_BIDEN_MARGIN) + 
                          "% (Tilt Democratic) - Democratic recapture");
        System.out.println("2024: Trump +" + MARGIN_FORMAT.format(NORTHAMPTON_2024_TRUMP_MARGIN) + 
                          "% (Lean Republican) - Republican re-flip");
        
        // Calculate Northampton volatility
        double northampton_2016_2020_swing = NORTHAMPTON_2016_TRUMP_MARGIN + NORTHAMPTON_2020_BIDEN_MARGIN;
        double northampton_2020_2024_swing = NORTHAMPTON_2020_BIDEN_MARGIN + NORTHAMPTON_2024_TRUMP_MARGIN;
        double northampton_total_volatility = northampton_2016_2020_swing + northampton_2020_2024_swing;
        
        System.out.println("Northampton Volatility: " + SWING_FORMAT.format(northampton_total_volatility) + 
                          "% combined swing (2016-2024)");
        System.out.println("Classification: GENUINE SWING TERRITORY");
        System.out.println();
        
        // PA-08 Cartwright progressive decline analysis (corrected)
        System.out.println("PA-08 CARTWRIGHT ELECTORAL DECLINE (CORRECTED):");
        System.out.println("2018: Cartwright +" + SWING_FORMAT.format(CARTWRIGHT_2018_MARGIN) + 
                          "% (Likely Democratic)");
        System.out.println("2020: Cartwright +" + SWING_FORMAT.format(CARTWRIGHT_2020_MARGIN) + 
                          "% (Lean Democratic)");
        System.out.println("2022: Cartwright +" + SWING_FORMAT.format(CARTWRIGHT_2022_MARGIN) + 
                          "% (Lean Democratic) ✓ CORRECTED");
        System.out.println("2024: Bresnahan +" + SWING_FORMAT.format(BRESNAHAN_2024_MARGIN) + 
                          "% (Lean Republican) - SEAT FLIP");
        
        // Calculate corrected Cartwright decline
        double cartwright_2018_2020_swing = CARTWRIGHT_2018_MARGIN - CARTWRIGHT_2020_MARGIN;
        double cartwright_2020_2022_swing = CARTWRIGHT_2020_MARGIN - CARTWRIGHT_2022_MARGIN;
        double cartwright_2022_2024_swing = CARTWRIGHT_2022_MARGIN + BRESNAHAN_2024_MARGIN;
        double cartwright_total_decline = CARTWRIGHT_2018_MARGIN + BRESNAHAN_2024_MARGIN;
        
        System.out.println("Progressive Decline: " + SWING_FORMAT.format(cartwright_total_decline) + 
                          "% total swing (2018-2024)");
        System.out.println("2020→2022 Swing: " + SWING_FORMAT.format(cartwright_2020_2022_swing) + 
                          "% (steady erosion) ✓ CORRECTED");
        System.out.println("Classification: CONSISTENT REPUBLICAN MOMENTUM");
        System.out.println();
        
        // Comparative analysis programming
        System.out.println("COMPARATIVE DISTRICT ANALYSIS:");
        System.out.println("PA-07 Pattern: Electoral volatility - genuine swing territory");
        System.out.println("PA-08 Pattern: Progressive decline - consistent Republican gains");
        System.out.println("Combined Significance: 12.0% and 11.4% swings demonstrate regional realignment");
        System.out.println();
        
        // MOVCalculator applications
        System.out.println("MOVCALCULATOR EDUCATIONAL APPLICATIONS:");
        System.out.println("• Data Accuracy Validation: Corrected 2022 margin shows steady decline pattern");
        System.out.println("• Volatility vs. Momentum: Programming logic to distinguish swing vs. trending districts");
        System.out.println("• Historical Context Integration: Multi-election temporal analysis capabilities");
        System.out.println("• Strategic Assessment: Resource allocation based on district trajectory patterns");
        System.out.println();
        
        System.out.println("PROFESSIONAL PROGRAMMING VALUE:");
        System.out.println("Demonstrates advanced conditional logic for complex electoral pattern analysis");
        System.out.println("essential for professional political analysis and campaign strategy applications.");
    }
    
    /**
     * Data accuracy validation methodology for political analysis
     * Demonstrates importance of precise historical data in temporal programming
     * 
     * Educational Objective: Professional standards for data validation
     * and accuracy requirements in real-world analytical applications
     */
    public static void validateHistoricalDataAccuracy() {
        System.out.println("HISTORICAL DATA VALIDATION METHODOLOGY");
        System.out.println("═══════════════════════════════════════════════════════════════════════");
        System.out.println();
        
        // Demonstrate impact of data correction
        double original_2022_margin = 3.8;  // Previously listed (incorrect)
        double corrected_2022_margin = CARTWRIGHT_2022_MARGIN;  // 2.4% (actual)
        double correction_impact = original_2022_margin - corrected_2022_margin;
        
        System.out.println("CARTWRIGHT 2022 DATA CORRECTION:");
        System.out.println("Original Analysis: Cartwright +3.8% (2022) - suggested stagnation");
        System.out.println("Corrected Analysis: Cartwright +2.4% (2022) - shows continued decline");
        System.out.println("Impact of Correction: " + SWING_FORMAT.format(correction_impact) + 
                          "% difference affects trend interpretation");
        System.out.println();
        
        // Calculate trend interpretation differences
        double original_trend_2020_2022 = CARTWRIGHT_2020_MARGIN - original_2022_margin;  // 0.0%
        double corrected_trend_2020_2022 = CARTWRIGHT_2020_MARGIN - corrected_2022_margin; // 1.4%
        
        System.out.println("TREND ANALYSIS IMPACT:");
        System.out.println("Original: 2020→2022 = " + SWING_FORMAT.format(Math.abs(original_trend_2020_2022)) + 
                          "% (no Republican gains)");
        System.out.println("Corrected: 2020→2022 = " + SWING_FORMAT.format(corrected_trend_2020_2022) + 
                          "% (consistent Republican momentum)");
        System.out.println("Predictive Value: Corrected data better explains 2024 defeat");
        System.out.println();
        
        System.out.println("PROGRAMMING BEST PRACTICES:");
        System.out.println("• Source Verification: Cross-reference official election records");
        System.out.println("• Temporal Consistency: Validate trend patterns for logical progression");
        System.out.println("• Impact Assessment: Evaluate how corrections affect strategic analysis");
        System.out.println("• Professional Standards: Accurate data essential for credible applications");
        System.out.println();
        
        System.out.println("EDUCATIONAL VALUE: Demonstrates critical importance of data validation");
        System.out.println("in professional programming applications requiring historical accuracy.");
    }
}

#### Pennsylvania Electoral History and Regional Realignment
The MarginofVictory calculator's rating system captures important electoral trends in Pennsylvania's suburban districts, particularly PA-01, PA-07, and PA-08, which have experienced significant political realignment over the past decade:

---

**Pennsylvania's 1st Congressional District (Bucks/Montgomery):**
- 2018 Senate: Casey (D) +13.8 (56.1-42.3)
- 2020 President: Biden (D) +4.6
- 2024 Senate: Casey (D) +0.9 (49.3-48.4)
- 2024 President: Harris (D) +0.4
- 2024: Bucks County flips Republican for the first time since 1988 by 291 votes; Montgomery County keeps district Democratic.
- Electoral Shift: PA-01 moved from Safe Democratic (+13.8%) to Tilt Democratic (+0.9%), a 12.9% swing toward Republicans (2018-2024)

**Pennsylvania's 7th Congressional District (Lehigh Valley):**
- 2016 President (Northampton): Trump (R) +3.78 (Lean Republican) - First Republican win since 1988
- 2018 Senate: Casey (D) +10.1 (54.2-44.1) (Safe Democratic)
- 2020 President (Northampton): Biden (D) +0.72 (Tilt Democratic)
- 2024 President (Northampton): Trump (R) +1.78 (Lean Republican)
- 2024 Senate: McCormick (R) +1.8 (49.6-47.8) (Lean Republican)
- 2024: Monroe County flips Republican for the first time since 2004.
- Electoral Shift: PA-07 moved from Safe Democratic (+10.2%) to Lean Republican (+1.8%), a 12.0% swing toward Republicans (2018-2024)

**Pennsylvania's 8th Congressional District (Scranton/Wilkes-Barre):**
- 2018 House: Cartwright (D) +9.8 (Likely Democratic)
- 2018 Senate: Casey (D) +6.2 (53.1-46.9) (Likely Democratic)
- 2020 House: Cartwright (D) +3.6 (Lean Democratic)
- 2020 President: Trump (R) +2.9 (District), Cartwright outperformed top of ticket
- 2022 House: Cartwright (D) +2.4 (Lean Democratic)
- 2024 House: Bresnahan (R) +1.6 (Lean Republican, flip)
- 2024 Senate: McCormick (R) +4.5 (52.25-47.75) (Lean Republican)
- 2024 President: Trump (R) ~+8.5 (Likely Republican)
- 2024: Monroe County flips Republican for the first time since 2004.
- Electoral Shift: PA-08 moved from Likely Democratic (+6.2%) to Lean Republican (+4.5%), a 10.7% swing toward Republicans (2018–2024)

---

**Summary Table:**

| District | 2018 | 2020 | 2022 | 2024 |
|----------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|
| PA-01    | Casey +13.8 (D)             | Biden +4.6 (D)              | —                           | Casey +0.9 (D), Harris +0.4 (D), Bucks flips R |
| PA-07    | Casey +10.2 (D)             | Biden +0.72 (D) (Northampton) | —                        | McCormick +1.8 (R), Trump +1.78 (R, Northampton) |
| PA-08    | Cartwright +9.8 (D), Casey +6.2 (D) | Cartwright +3.6 (D), Trump +2.9 (R) | Cartwright +2.4 (D) (corrected) | Bresnahan +1.6 (R) (flip), McCormick +4.5 (R), Trump +8.5 (R) |

---

- **PA-01:** Casey +13.8 (2018), Biden +4.6 (2020), Casey +0.9 (2024), Harris +0.4 (2024), Bucks County flips Republican for the first time since 1988, Montgomery County keeps district Democratic.
- **PA-07:** Casey +10.2 (2018), Biden +0.72 (2020, Northampton), McCormick +1.8 (2024), Trump +1.78 (2024, Northampton), shows volatility and swing status.
- **PA-08:** Cartwright +9.8 (2018), Casey +6.2 (2018), Cartwright +3.6 (2020), Trump +2.9 (2020), Cartwright +2.4 (2022, corrected), Bresnahan +1.6 (2024, flip), McCormick +4.5 (2024), Trump +8.5 (2024).

**Combined Trend Pattern**: PA-07, PA-08, and PA-01 all show consistent rightward movement, with PA-01 voting Republican for the first time since 1988 in Bucks County in 2024. Notably, Senator Casey won PA-01 by **+13.8** (56.1-42.3) in 2018, but his margin shrank to just **+0.9** (49.3-48.4) in 2024. Biden carried PA-01 by **+4.6** in 2020, and Harris by only **+0.4**. The Bucks County portion flipped Republican, but the Montgomery County portion kept the district from flipping outright. This indicates broader regional realignment rather than candidate-specific effects. This demonstrates how the MarginCalculator's systematic rating approach captures both individual race competitiveness and broader electoral patterns.

**Split-Ticket Voting Implications**: The substantial ticket-splitting in PA-08 (Trump +8.49% vs. Cartwright's competitive showing) suggests that while these districts have moved rightward presidentially, they remain competitive for down-ballot Democratic candidates who maintain personal relationships with constituents.

**Forecasting Applications**: These Pennsylvania examples demonstrate how historical MarginCalculator data can identify districts experiencing realignment, allowing analysts to adjust future race ratings based on demonstrated voting pattern shifts.

#### Historical Context
**Virginia House of Delegates (2017)**: Multiple races decided by fewer than 100 votes, with one race initially ending in a tie and decided by drawing names from a bowl, illustrating the real-world impact of ultra-close margins in determining legislative control.

### Race Rating Methodology

The application uses the following margin thresholds for race classification, based on industry-standard political analysis:

- **Tossup**: ≤ 0.5% (Extremely competitive, often triggers recounts)
- **Tilt**: 0.51% - 0.99% (Slight advantage, high uncertainty)
- **Lean**: 1.0% - 5.5% (Modest lead, competitive but favored)
- **Likely**: 5.6% - 10.0% (Strong lead, low probability of upset)
- **Safe**: > 10.0% (Overwhelming lead, virtually certain outcome)

## Real-World Applications

### Political Analysis Use Cases
1. **Campaign Strategy**: Resource allocation based on race competitiveness
2. **Media Coverage**: Professional race rating for election reporting
3. **Academic Research**: Electoral analysis for political science studies
4. **Redistricting Analysis**: Evaluate competitiveness of proposed district boundaries
5. **Election Forecasting**: Historical data analysis for future predictions

## Academic Context and Learning Outcomes

### Educational Objectives
This project demonstrates mastery of fundamental programming concepts taught in CPT-236:

- **Advanced Input Validation**: While loops, range checking, and error handling
- **Mathematical Programming**: Absolute value calculations and threshold logic
- **Conditional Logic**: Complex if-else structures for classification systems
- **Professional Documentation**: Industry-standard commenting and code organization

### Learning Progression
The MarginCalculator project represents an exploratory application of course concepts:

1. **Foundation Phase**: Basic Java syntax and I/O (GetCost.java, ChiliToGo.java)
2. **Development Phase**: Conditional logic and formatting (Weekly_Pay.java, Commission.java)
3. **Collaboration Phase**: Team programming experience (DeesChickenShack.java with Charles Davis)
4. **Exploration Phase**: Political analysis application (v1.0 prototype)
5. **Enhancement Phase**: Professional features and copyright protection (v2.0)

## Installation and Usage

### Prerequisites
- Java Development Kit (JDK) 8 or higher
- Command line interface or Java IDE

### Compilation and Execution
```bash
# Compile the application
javac MarginCalculator.java

# Run the application
java MarginCalculator
```

### Usage Example
```
Enter vote percentage for: Democrat (D): 52.3
Enter vote percentage for: Republican (R): 47.1
Democrat (D): 52.30%
Republican (R): 47.10%
The margin of victory is: 5.20%
Democrat (D) is the winner. Race rating: Lean Democratic
```

## Version History

### v2.0 (Enhanced Version) - Current
- **Copyright Protection**: Professional legal framework
- **Enhanced Interface**: Improved user experience and formatting
- **Advanced Validation**: Comprehensive error handling
- **Professional Output**: Industry-standard race analysis presentation
- **Documentation**: Complete development history and academic integration

### v1.0 (Prototype Version) - July 3, 2025
- **Core Functionality**: Basic margin calculation and race rating
- **Input Validation**: While loops for percentage range checking
- **DecimalFormat**: Professional percentage formatting
- **Educational Focus**: Demonstrates programming concepts applied to political analysis

## Academic Citations and References

### Political Analysis Standards
1. **Cook Political Report**: Industry-standard race rating methodology
2. **Sabato's Crystal Ball (UVA Center for Politics)**: Electoral analysis framework
3. **FiveThirtyEight**: Statistical modeling and election forecasting

### Real-World Case Study Sources

The real-world case studies referenced in this documentation are based on official election results and credible news sources:

**[1]** North Carolina State Board of Elections. "Official Election Results - 2024 General Election." North Carolina State Board of Elections, 2024. Accessed July 2025.

**[2]** Riggs v. Stein, North Carolina Supreme Court Case No. 413A24. Court filings and litigation timeline, 2024-2025.

**[3]** Iowa Secretary of State. "Official Results - 2020 General Election, U.S. House District 2." Iowa Secretary of State's Office, 2020.

**[4]** Associated Press. "Iowa's 2nd District race decided by 6 votes after recount." Associated Press, November 2020.

**[5]** Nevada Secretary of State. "Official Election Results - 2022 General Election, U.S. Senate." Nevada Secretary of State's Office, 2022.

**[6]** The Nevada Independent. "Election Day snowstorm affects northern Nevada turnout in tight races." The Nevada Independent, November 2022.

**[7]** Virginia Department of Elections. "Official Results - 2017 General Election, House of Delegates." Virginia Department of Elections, 2017.

**[8]** The Washington Post. "Virginia House race ends in tie, winner decided by drawing names." The Washington Post, January 2018.

**[9]** Pennsylvania Department of State. "Official Election Results - 2024 General Election, 8th Congressional District." Pennsylvania Department of State, 2024.

**[10]** California Secretary of State. "Official Election Results - 2024 General Election, 45th Congressional District." California Secretary of State, 2024.

**[11]** Florida Division of Elections. "Official Election Results - 2018 General Election, Governor." Florida Division of Elections, 2018.

**[12]** Pennsylvania Department of State. "Official Election Results - 2024 General Election, U.S. Senate." Pennsylvania Department of State, 2024.

**[13]** Associated Press. "Pennsylvania Senate race heads to recount as Casey challenges results." Associated Press, November 2024.

**Note**: All vote counts, margins, and contextual details are derived from official state election records and verified news sources. Weather impact assessments are based on contemporaneous news reporting and political analysis.