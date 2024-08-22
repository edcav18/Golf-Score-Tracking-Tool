import Hole

class Scorecard():
    """Class to represent a golf scorecard"""

    def __init__(self,
                 date="",
                 course_name="",
                 tot_holes=0,
                 course_par=0):
        """
        Initialize a Scorecard object with date, 
        course name, total holes and course par
        """
        self.date = date
        self.course_name = course_name
        self.total_holes = tot_holes
        self.__course_par = course_par
        self.__total_score = 0
        self.hole_list = []
        self.total_putts = 0
        self.fairways_in_reg = 0
        self.greens_in_reg = 0
    
    def calculate_score(self):
        """Calculate the total score for the scorecard"""
        for hole in self.hole_list:
            self.__total_score += int(hole.hole_score)

    def calculate_putts(self):
        """Calculate the total number of putts for the scorecard"""
        for hole in self.hole_list:
            self.total_putts += int(hole.hole_putts)

    def calculate_fir(self):
        """Calculate the fairways in regulation for the scorecard"""
        for hole in self.hole_list:
            if hole.fairway_in_reg == "yes":
                self.fairways_in_reg += 1

    def calculate_gir(self):
        """Calculate the greens in regulation for the scorecard"""
        for hole in self.hole_list:
            if hole.green_in_reg == "yes":
                self.greens_in_reg += 1

    def __str__(self):
        """Return scorecard represented as a formatted string"""
        header = ("Date: {}        Course Name: {}       "
                  "Holes: {}       Par: {}\n".format(self.date, self.course_name, self.total_holes, self.__course_par))
        separator = "——————————————————————————————\
———————————————————————————————————————————————\n"
        column_headers = ("Hole:     Par:     Score:     Fairway in regulation:     "
                          "Green in regulation:\n")
        line_separator = "————      ————     —————      —————————————————————      ————————————————————\n"

        holes_info = ""
        for hole in self.hole_list:
            holes_info += "#{:^4}     {:^4}     {:^5}      {:^21}      {:^20}\n".format(hole._Hole__hole_number, hole.hole_par, hole.hole_score, hole.fairway_in_reg, hole.green_in_reg)
        
        totals = "Total score: {}     Total putts: {}    Fairways in regulation: {}     Greens in regulation: {} ".format(self.__total_score, self.total_putts, self.fairways_in_reg, self.greens_in_reg)

        return header + separator + column_headers + line_separator + holes_info + separator + "\n" + totals

    def __lt__(self, other):
        """
        Less than comparison method, to add score comparison feature
        across scorecards
        """
        return self.__total_score < other.__total_score