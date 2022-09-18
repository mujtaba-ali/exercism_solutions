plant_names = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}


class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David",
                                             "Eve", "Fred", "Ginnie", "Harriet",
                                             "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram.splitlines()
        self.students = {student: [] for student in sorted(students)}
        self.assign()


    def assign(self):
        for i, j in zip(range(0, 24, 2), self.students.keys()):
            self.students[j] = [self.diagram[x][i+k:i+(k+1)] for x in [0, 1] for k in [0, 1]]


    def plants(self, name):
        return [plant_names[i] for i in self.students[name]]
