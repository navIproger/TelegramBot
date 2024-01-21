import datetime as dt


def get_day():
    day = dt.datetime.now().isocalendar()[2]
    if day == 6:
        return 5
    elif day == 7:
        return 1
    return int(day)


def position_of_schedule():
    first_numerical = dt.date(2024, 1, 22).isocalendar()[1]
    current_week = dt.datetime.now().isocalendar()[1]
    if (current_week - first_numerical) % 4 == 0:
        return 3
    elif (current_week - first_numerical) % 4 == 1:
        return 4
    elif (current_week - first_numerical) % 4 == 2:
        return 5
    elif (current_week - first_numerical) % 4 == 3:
        return 6
