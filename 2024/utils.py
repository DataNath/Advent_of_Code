import requests, os, datetime as dt
from dotenv import load_dotenv

load_dotenv("../.venv/.env")
cookie = os.environ.get("COOKIE")

year_today = dt.date.today().year
day_today = dt.date.today().day

def fetch_daily_data(year=None, day=None):
    selected_year = year_today if year is None else year
    selected_day = day_today if day is None else day

    url = f"https://adventofcode.com/{selected_year}/day/{selected_day}/input"

    if selected_year > year_today or selected_day not in range(1,26):
        print("You have provided a year in the future or a day outside of 1-25.")
        exit()

    response = requests.get(
        url,
        cookies={"session": cookie},
        headers={"User-Agent": "https://github.com/DataNath/Advent_of_Code by Nathan.p100@hotmail.co.uk", "charset": "utf-8", "Content-Type": "Application/json"},
    )

    if response.status_code == 200:

        data = response.text.strip()

        os.makedirs("inputs", exist_ok=True)
        file = open(f"inputs/Day {selected_day}.txt", 'w')
        file = file.write(data)

    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")
