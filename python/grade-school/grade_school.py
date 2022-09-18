import bisect, itertools


class School:
    def __init__(self):
        self.roster_data = [[] for i in range(12)]


    def add_student(self, name, grade):
        bisect.insort(self.roster_data[grade], name)


    def roster(self):
        return list(itertools.chain.from_iterable(self.roster_data))


    def grade(self, grade_number):
        return self.roster_data[grade_number].copy()
