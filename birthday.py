from datetime import datetime


def get_birthdays_per_week(users):
    next_week_birthdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if delta_days > 6:
            continue

        day_of_week = birthday_this_year.strftime("%A")
        if day_of_week == "Saturday" or day_of_week == "Sunday":
            next_week_birthdays["Monday"].append(name)
        else:
            next_week_birthdays[day_of_week].append(name)

    for week_day, names in next_week_birthdays.items():
        print(f"{week_day}: {', '.join(names)}")
