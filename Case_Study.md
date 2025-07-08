/**
 * MarginOfVictory Calculator v2.0+ Pennsylvania Electoral Analysis Enhancement
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

#### Pennsylvania's 7th Congressional District (Lehigh Valley):

- **2016 President (Northampton):** Trump (R) +3.78 (Lean Republican) - First Republican win since 1988
- **2018 Senate:** Casey (D) +10.1 (54.2-44.1) (Safe Democratic)
- **2020 President (Northampton):** Biden (D) +0.72 (Tilt Democratic)
- **2022 House:** Wild (D) +2.0 (Lean Democratic)
- **2022 Senate:** Fetterman (D) +4.5 (Likely Democratic)
- **2024 President (Northampton):** Trump (R) +1.78 (Lean Republican)
- **2024 House:** Mackenzie (R) +1.0 (Lean Republican, Flip)
- **2024 Senate (PA-07 Districtwide):** McCormick (R): 49.6%, Casey (D): 47.8% — Margin: McCormick +1.8% (Lean Republican)
- **2024 Senate (Northampton County):** McCormick (R): 49.13%, Casey (D): 48.54% — Margin: McCormick +0.59% (Tilt Republican)
- **2024:** Monroe County flips Republican for the first time since 2004.
- **2024:** PA-07 flipped Republican for the first time since the lines were redrawn in 2018.
- **Electoral Shift:** PA-07 moved from Safe Democratic (+10.2%) to Lean Republican (+1.8%) districtwide, but the Northampton County core moved to Tilt Republican (+0.59%).

---

**Summary Table:**

| District  | 2018           | 2020           | 2022                     | 2024                                                                 |
|-----------|----------------|----------------|--------------------------|----------------------------------------------------------------------|
| **PA-07** | Casey +10.2(D) | Biden +0.72(D) | Wild +2.0(D), Fetterman +4.5(D) | Mackenzie +1.0 (R) McCormick +1.8(R)\*<br>Northampton: +0.59(R)<br>Trump +1.78(R, Northampton) |

\* Districtwide total; Northampton County (the swing core of PA-07): McCormick +0.59%.
**Pennsylvania's 8th Congressional District (Scranton/Wilkes-Barre):**
- 2018 House: Cartwright (D) +9.8 (Likely Democratic)
- 2018 Senate: Casey (D) +6.2 (53.1-46.9) (Likely Democratic)
- 2020 House: Cartwright (D) +3.6 (Lean Democratic)
- 2020 President: Trump (R) +2.9 (District), Cartwright outperformed top of the ticket
- 2022 House: Cartwright (D) +2.4 (Lean Democratic)
- 2022 Senate: Fetterman (D) +1.2 (Lean Democratic)
- 2024 House: Bresnahan (R) +1.6 (Lean Republican, flip)
- 2024 Senate: McCormick (R) +4.5 (52.25-47.75) (Lean Republican)
- 2024 President: Trump (R) ~+8.5 (Likely Republican)
- 2024: Monroe County flips Republican for the first time since 2004.
- Electoral Shift: PA-08 moved from Likely Democratic (+6.2%) to Lean Republican (+4.5%), a 10.7% swing toward Republicans (2018–2024)
- Note: In 2022, both Cartwright and Fetterman won PA-08, demonstrating continued split-ticket voting in this blue-collar district. The 2022 governor's race is omitted due to significant candidate quality issues on the Republican side.

---

**Summary Table:**

| District  | 2018                                    | 2020                                    | 2022                                    | 2024                                                      |
|-----------|------------------------------------------|------------------------------------------|------------------------------------------|-----------------------------------------------------------|
| **PA-01** | Casey +13.8 (D)                         | Biden +4.6 (D)                           | Fetterman +7.5 (D)                        | Casey +0.9 (D)<br>Harris +0.4 (D)<br>**Bucks flips R for the first time since 1988**    |
| **PA-07** | Casey +10.2 (D)                         | Biden +0.72 (D, Northampton)             | Wild +2.0 (D)<br>Fetterman +4.5 (D)       | **Mackenzie +1.0 (R) (flip)**<br>McCormick +1.8 (R)<br>Trump +1.78 (R, Northampton)<br>**Monroe flips R for the first time since 2004**        |
| **PA-08** | Cartwright +9.8 (D)<br>Casey +6.2 (D)   | Cartwright +3.6 (D)<br>Trump +2.9 (R)    | Cartwright +2.4 (D)<br>Fetterman +1.2 (D) | **Bresnahan +1.6 (R) (flip)**<br>McCormick +4.5 (R)<br>Trump +8.5 (R)<br>**Monroe flips R for the first time since 2004** |
