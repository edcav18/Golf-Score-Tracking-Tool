"""
Edoardo Cavallero
Class: CS 521 - Spring 2
Date: 4/24/24
Final Project
Description: Golf score tracking tool
"""
import functions
import os
import sys
import pickle
from Hole import Hole
from Scorecard import Scorecard

# Define file path for storing score data
FILE_PATH = "scores_data.pkl"
USERS_DATA = "recorded_users.pkl"

# Create a test Scorecard
scorecard_test = Scorecard()
# Create a test Hole and append it to the hole list of test Scorecard
hole_test = Hole(putts = 2, score = 5)
scorecard_test.hole_list.append(hole_test)

# Calculate the total score and putts for the scorecard
scorecard_test.calculate_score()
scorecard_test.calculate_putts()

# Assert statement to check if methods work as expected
assert scorecard_test._Scorecard__total_score == 5
assert scorecard_test.total_putts == 2
print("Scorecard test successful.")

# Test less than method for Scorecard class
scorecard_test2 = Scorecard()
scorecard_test2._Scorecard__total_score = 4
assert scorecard_test2._Scorecard__total_score\
      < scorecard_test._Scorecard__total_score

# Prompt user to enter username
username = input("Welcome to PythonPutts 1.0!\n\
Please enter your username to start: ")

# Load existing data from username pickle file, if any
try:
    with open(USERS_DATA, 'rb') as f:
        username_list = pickle.load(f)
except FileNotFoundError:
    username_list = set()
except EOFError:
    username_list = set()

# Add username to username set
username_list.add(username)

# Save username set
with open(USERS_DATA, 'wb') as f:
        pickle.dump(username_list, f)

# Prompt user to choose an action
action = functions.validate_action("What would you like to do? Enter 1 to enter a new score or 2 \
to view previous scores")

if action == "1": # If user chooses to enter a new score
    # Create a new scorecard
    my_scorecard = functions.create_scorecard()

    # Add data for each hole in the course played
    functions.add_holes_data(my_scorecard)

    # Calculate additional statistics for the round
    my_scorecard.calculate_score()
    my_scorecard.calculate_putts()
    my_scorecard.calculate_gir()
    my_scorecard.calculate_fir()


    print()
    print("Your Scorecard: ")
    print()
    print("User: {}".format(username))
    print(my_scorecard)
    print()
    save = functions.validate_yes_no("Save scorecard? (yes/no): ")


    try:
        # Load existing data from pickle file, if any
        with open(FILE_PATH, 'rb') as f:
            rounds_log = pickle.load(f)
    except FileNotFoundError:
        rounds_log = dict()
    except EOFError:
        rounds_log = dict()
    if save == "yes":
        # If the user wants to save, add scorecard to rounds_log dictionary
        if (my_scorecard.date, username) in rounds_log:
            rounds_log[(my_scorecard.date, username)].append(my_scorecard)
        else:
            rounds_log[(my_scorecard.date, username)] = [my_scorecard]
        # Save the updated rounds dictionary to the pickle file
        with open(FILE_PATH, "wb") as pkl_file:
            pickle.dump(rounds_log, pkl_file)
        print("Scorecard saved!")
        sys.exit()
    else: # If user wants to discard score, exit
        print("See you next time!")
        sys.exit()

else: # If user chooses to view previous scores
    print()
    try:
        # Load the dictionary from the pickle file
        with open('scores_data.pkl', 'rb') as f:
            scores_data = pickle.load(f)

        # Sort the dictionary by keys
        scores_data = dict(sorted(scores_data.items()))

        # Iterate over the items in the dictionary and print them
        found = False
        for key, value_list in scores_data.items():
            if username in key:
                found = True
                for value in value_list:
                    print(f"User: {key[1]}\n{value}")
                print("\n")

        if not found:  # If user does not have any previous scores
            print("No scores found for this username.")
    except FileNotFoundError:
        print("Error: file not found.")
        sys.exit()
    except EOFError:
        print("No previous scores found.")
        sys.exit()
    except AttributeError:
        print("File corrupted. Erasing log file...")
        os.remove("scores_data.pkl")
        print("Corrupted file removed. Please try again.")
        sys.exit()
    except pickle.UnpicklingError:
        print("File corrupted. Erasing log file...")
        os.remove("scores_data.pkl")
        print("Corrupted file removed. Please try again.")
        sys.exit()
