class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.final_min = minute % 60
        self.final_hr = int((((minute-self.final_min)/60)+hour)%24)

    def __repr__(self):
        return f"{self.final_hr:02d}:{self.final_min:02d}"

    def __eq__(self, other):
        return (self.final_hr == other.hour and self.final_min == other.minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

