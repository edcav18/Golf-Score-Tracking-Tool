from datetime import datetime
from Scorecard import Scorecard
from Hole import Hole

def create_scorecard():
    """
    Initialize a scorecard object prompting 
    user for details and validating input
    """
    round_date = validate_date("Date of your round (MM/DD/YYYY): ")
    course_name = input("Course name: ")
    total_holes = validate_int_input("Total holes")
    course_par = validate_int_input("Course par")
    my_scorecard = Scorecard(round_date, course_name, total_holes, course_par)
    return my_scorecard


def add_holes_data(my_scorecard):
    """
    Add a list of hole objects to the scorecard prompting the user
    for score details about each hole and validating input
    """
    for i in range(my_scorecard.total_holes):
        print("Hole #{}".format(i+1))
        par = validate_int_input("Enter the par for this hole")
        score = validate_int_input("Enter your score for this hole")
        putts = validate_int_input("Enter the total number of putts")
        
        if int(par) > 3:
            fir = validate_yes_no("Fairway in regulation? (yes/no)")
        else:
            fir = "Par 3"
        
        gir = validate_yes_no("Green in regulation? (yes/no)")
        
        hole_data = Hole(i+1, par, score, putts, fir, gir)
        my_scorecard.hole_list.append(hole_data)

def validate_int_input(var_name):
    """Validate integer input"""
    while True:
        user_input = input(f"{var_name}: ")
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        user_input = int(user_input)
        if user_input < 0:
            print(f"{var_name} must be a positive integer.")
            continue
        break
    return user_input

def validate_yes_no(var_name):
    """Validate input for yes or no question"""
    while True:
        user_input = input(f"{var_name}: ").lower()
        if user_input != "yes" and user_input != "no":
            print("Invalid input. Please enter either 'yes' or 'no'")
            continue
        break
    return user_input

def validate_action(var_name):
    """Validate input for user action prompt"""
    while True:
        user_input = input(f"{var_name}: ").lower()
        if user_input != "1" and user_input != "2":
            print("Invalid input. Please enter '1' to enter a new score or '2' to view previous scores.")
            continue
        break
    return user_input

def validate_date(var_name):
    """Validate input for round date"""
    while True:
        user_input = input(f"{var_name}: ").lower()
        try:
            date = datetime.strptime(user_input, "%m/%d/%Y").date()
        except ValueError:
            print("Invalid input. Please enter date in format MM/DD/YYYY")
            continue
        break
    return date