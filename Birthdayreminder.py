import datetime
import json

def check_birthdays(file="birthdays.json"):
    today = datetime.datetime.today().strftime('%m-%d')
    with open(file) as f:
        birthdays = json.load(f)

    for name, date in birthdays.items():
        if date == today:
            print(f"🎉 Today is {name}'s birthday!")


