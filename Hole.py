class Hole():
    """Class to represent a golf hole"""
    def __init__(self,
                 h_num=0,
                 par=0,
                 score=0,
                 putts=0,
                 fir="",
                 gir =""):
        """
        Initialize  a hole object with hole number,
        par for the hole, score for the hole, putts for the hole,
        whether a fairway was hit in regulation, whether a green
        was hit in regulation
        """
        self.__hole_number = h_num
        self.hole_par = par
        self.hole_score = score
        self.__over_par = self.__score_over_par()
        self.hole_putts = putts
        self.fairway_in_reg = fir
        self.green_in_reg = gir

    def __score_over_par(self):
        """Calculate the number of strokes score is over par for the hole"""
        over_par = int(self.hole_score) - int(self.hole_par)
        return over_par