import calendar
from datetime import date as dt


def add_zeroes(week1, week2):
    while len(week1) != 7:
        week1.insert(0, 0)
        
    while len(week2) != 7:
        week2.append(0)

    return week1, week2


class MeetupDayException(RuntimeError):
    def __init__(self, arg):
        self.args = arg


def meetup(year, month, week, day_of_week):
    c = calendar.TextCalendar(calendar.SUNDAY)
    cal = c.formatmonth(year, month)
    l = cal.splitlines()[2:]
    first_week = [int(i) for i in l[0].split()]
    last_week = [int(i) for i in l[-1].split()]
    mid_weeks = [[int(i) for i in j.split()] for j in l[1:-1]]
    weeks = []
    days = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3,
            "Thursday": 4, "Friday": 5, "Saturday": 6}

    week1, week2 = add_zeroes(first_week, last_week)
    weeks.append(week1)
    for i in mid_weeks: weeks.append(i)
    weeks.append(week2)

    dates_on_day = [i[days[day_of_week]] for i in weeks]
    dates_wo_zeroes = [i for i in dates_on_day if i != 0]
    try:
        if week == "last":
            date = dates_wo_zeroes[-1]
        elif week == "teenth":
            for i in dates_wo_zeroes: 
                if i in range(13, 20): 
                    date = i
                    break
        else:
            date = dates_wo_zeroes[int(week[0]) - 1] 
    except IndexError as err:
        raise MeetupDayException(err.args)
    return dt(year, month, date)


