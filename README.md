# Golf-Score-Tracking-Tool

This is a program I created for a term project. It is an application called “Python Putts” that allows the user to enter a variety of details and scoring statistics about a round of golf. The application then compiles the information entered by the user into a formatted scorecard which is stored in a pickle file under the user’s username. Users can then print all of the rounds they have entered into the application to track their progress.

The program begins by prompting the user for their username, and lets them select two options: enter a new score or view previous scores.
If the user elects to enter a new score, the application prompts them for the date of the round, the name of the course, course par and the total number of holes on the course. It then asks for information about each hole, including the par for the hole, the score the user shot on the hole, whether they hit the green in regulation (ie in 1 shot for a par 3, 2 shots for a par 4 or 3 shots for a par 5) and, if the par for the hole is higher than 3, if they hit the fairway off the tee (fairway in regulation).

Once the information has been entered, the program displays a formatted scorecard with all of the above information, and asks the user whether they want to save their score, saving the scorecard to an output file if desired and exiting the program if not. 

If the user elects to view their previous scores, the program prints a list of the formatted scorecards available in the log file under that username, unless no scores are found for the user which prints an error message.

This program is a powerful tool for golfers who want to lower their scores, as it provides them with a snapshot of several statistics that can inform them on what aspects of their game they most need to practice. The structure of the classes and methods implemented in the program leaves room for adding several additional features, such as practice recommendations based on score statistics (eg. putting practice if more than two putts per hole are logged for more than three holes), tracking improvement over time, or calculating the user’s handicap index according to USGA specifications.
