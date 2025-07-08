//Name: Shamar Davis
//Date: July 7, 2025
//Purpose: Create a program that displays the state abbreviation, district number, candidate and who won.

//input: Prompt the user to enter the state abbreviation and district (state String, districtNumber int).
//Prompt user for the first candidate's name along with party affiliation and store it in a String variable. Candidate1, Candidate2, partyAffiliation1, partyAffliation2 String

//processing: Calculate the margin and determine the winner


import java.text.DecimalFormat;
import java.util.Scanner;

public class MarginOfVictory  {
    public static void main (String[] args) {
        Scanner inputDevice = new Scanner(System.in);
        //Prompt the user to enter the state abbreviation and district.
        System.out.print("State Abbreviation: ");
        String state = inputDevice.next().toUpperCase();
        inputDevice.nextLine(); // consume the leftover newline
        System.out.print("District Number: ");
        int districtNumber = inputDevice.nextInt();
        inputDevice.nextLine(); // consume leftover newline

        //Prompt user for the first candidate's name along with party affiliation and store it in a String variable.
        System.out.print("Enter the first candidate's name: ");

        String Candidate1 = inputDevice.nextLine();
        System.out.println("Enter the second candidate's name: ");

        String Candidate2 = inputDevice.nextLine();
        System.out.print("What is the party affiliation of " + Candidate1 + "? ");
        String partyAffiliation1 = inputDevice.nextLine();
        System.out.println(Candidate1 + " is a " + partyAffiliation1 + ".");
        System.out.print("What is the party affiliation of " + Candidate2 + "? ");
        String partyAffiliation2 = inputDevice.nextLine();
        System.out.println(Candidate2 + " is a " + partyAffiliation2 + ".");
        //Prompt the use to enter the incumbent party?
        System.out.println("Which party has the incumbency? ");
        String incumbentParty = inputDevice.nextLine();
        //get the right decimal format for the results and shorten the output.
        DecimalFormat df = new DecimalFormat("0.00");
        //Get the vote percentage with confirmation of accuracy.
        double votes1 = getVotePercentage(inputDevice, Candidate1);
        double votes2 = getVotePercentage(inputDevice, Candidate2);
        //Calculate the margin and determine the winner
        double margin = Math.abs(votes1 - votes2);
        String winner = votes1 > votes2 ? Candidate1 : Candidate2;
        String winnerParty = votes1 > votes2 ? partyAffiliation1 : partyAffiliation2;

        String rating = getRaceRating(margin);

        // Display results with professional formatting
        System.out.println("\n--- Election Results ---");
        System.out.println("State: " + state + " | District: " + districtNumber);
        System.out.println(Candidate1 + " (" + partyAffiliation1 + "): " + df.format(votes1) + "%");
        System.out.println(Candidate2 + " (" + partyAffiliation2 + "): " + df.format(votes2) + "%");
        System.out.println("Margin of Victory: " + df.format(margin) + "%");

        if (votes1 == votes2) {
            System.out.println("It's a tie! Race Rating: " + rating);
        } else {
            System.out.println(winner + " (" + winnerParty + ") is the winner. Race rating: " + rating + " " + winnerParty);
            if (!winnerParty.equalsIgnoreCase(incumbentParty)) {
                System.out.println("** FLIP: " + winnerParty + " gains this seat! **");
            }
            // Display closing message and close input device for resource management
            System.out.println("Thank you for using Margin of Victory calculator!");
            inputDevice.close();
        }
    }

    /**
     * Prompts the user for a candidate's vote percentage and validates input.
     * Ensures the percentage is between 0 and 100.
     * 
     * @param inputDevice Scanner for user input
     * @param candidateName Name of the candidate for prompt clarity
     * @return Validated vote percentage as a double
     */
public static double getVotePercentage(Scanner inputDevice, String candidateName) {
    double percentage = -1;
    while (true) {
        System.out.print("Enter the vote percentage for " + candidateName + " (0-100): ");
        if (inputDevice.hasNextDouble()) {
            percentage = inputDevice.nextDouble();
            inputDevice.nextLine(); // consume newline
            if (percentage >= 0 && percentage <= 100) {
                break;
            } else {
                System.out.println("Please enter a value between 0 and 100.");
            }
        } else {
            System.out.println("Invalid input. Please enter a numeric value.");
            inputDevice.next(); // consume invalid input
        }
    }
    return percentage;
}

/**
* Determines the race rating based on the margin of victory.
* 
* @param margin The absolute margin of victory as a percentage
* @return The industry-standard race rating
*/
public static String getRaceRating(double margin) {
    // Margin thresholds based on industry standards
    if (margin < 0.5) {
        return "Tossup";
    } else if (margin < 1.0) {
        return "Tilt";
    } else if (margin < 5.5) {
        return "Lean";
    } else if (margin < 10.0) {
        return "Likely";
    } else {
        return "Safe";
    }
}
}