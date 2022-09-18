class School:
    def __init__(self):
        self.roster_arr = []


    def __setitem__(self, idx, value):
        if key not in self.roster_dict.keys():
            self.roster_dict[key] = [value]
        else:
            self.roster_dict[key].append(value)


    def __getitem__(self, key=None):
        if not key and bool(self.roster_dict):
            for key, val in self.roster_dict.items():
                if len(self.roster_dict[key]) > 1:
                    self.roster_dict[key] = sorted(self.roster_dict[key])
            return [ele for (key, value) in sorted(self.roster_dict.items()) for ele in value]
        if key in self.roster_dict.keys():
            if len(self.roster_dict[key]) > 1:
                self.roster_dict[key] = sorted(self.roster_dict[key])
            return self.roster_dict[key]
        return []


    def add_student(self, name, grade):
        self.__setitem__(grade, name)


    def roster(self):
        return self.__getitem__()


    def grade(self, grade_number):
        return self.__getitem__(grade_number)

