class Student:
    def __init__(self, name : str, scores : list):
        """Displays a student name and their scores."""
        self.name = name
        self.scores = scores
    def calculate_avg(self)-> float:
        """Calculates the average scores of the student."""
        return sum(self.scores/len(self.scores))
    def is_passing(self)-> bool:
        """Checks the status if the students pass all the subjects."""
        passing_score = 40
        return all(score >= passing_score for score in self.scores)
class Performance_tracker:
    """Displays a new performance tracker object with an empty dictionary of students."""
    self.students = {}
    def add_student(self, student):
        """Adds a new student to the performance tracker."""
        

