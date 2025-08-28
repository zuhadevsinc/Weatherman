from utils import month_names


def draw_charts(all_records, year, month):

    month_records = []
    for r in all_records:
        if r["year"] == year and r["month"] == month:
            month_records.append(r)

    if not month_records:
        print("No data found for", year, "/", month)
        return

    hottest_day = None
    coldest_day = None

    for r in month_records:
        if r["max_temp"] not in (None, ""):
            if hottest_day is None or r["max_temp"] > hottest_day["max_temp"]:
                hottest_day = r
        if r["min_temp"] not in (None, ""):
            if coldest_day is None or r["min_temp"] < coldest_day["min_temp"]:
                coldest_day = r

    print(month_names[month], year, "\n")

    # ANSI color codes
    RED = "\033[0;31m"
    BLUE = "\033[0;34m"
    RESET = "\033[0m"

    # bars for hottest day
    if hottest_day:
        day_str = hottest_day["day"]
        if hottest_day["max_temp"] not in (None, ""):
            bar = "+" * int(hottest_day["max_temp"])
            print(f"{day_str} {RED}{bar}{RESET} {int(hottest_day['max_temp'])}C")
        if hottest_day["min_temp"] not in (None, ""):
            bar = "+" * int(hottest_day["min_temp"])
            print(f"{day_str} {BLUE}{bar}{RESET} {int(hottest_day['min_temp'])}C")

    # bars for coldest day
    if coldest_day:
        day_str = coldest_day["day"]
        if coldest_day["max_temp"] not in (None, ""):
            bar = "+" * int(coldest_day["max_temp"])
            print(f"{day_str} {RED}{bar}{RESET} {int(coldest_day['max_temp'])}C")
        if coldest_day["min_temp"] not in (None, ""):
            bar = "+" * int(coldest_day["min_temp"])
            print(f"{day_str} {BLUE}{bar}{RESET} {int(coldest_day['min_temp'])}C")


def draw_combined_charts(all_records, year, month):

    month_records = []
    for r in all_records:
        if r["year"] == year and r["month"] == month:
            month_records.append(r)

    if not month_records:
        print("No data found for", year, "/", month)
        return

    hottest_day = None
    coldest_day = None

    for r in month_records:
        if r["max_temp"] not in (None, ""):
            if hottest_day is None or r["max_temp"] > hottest_day["max_temp"]:
                hottest_day = r
        if r["min_temp"] not in (None, ""):
            if coldest_day is None or r["min_temp"] < coldest_day["min_temp"]:
                coldest_day = r

    print(month_names[month], year, "\n")

    # ANSI color codes
    RED = "\033[0;31m"
    BLUE = "\033[0;34m"
    RESET = "\033[0m"

    # bars for hottest day
    if hottest_day:
        day_str = hottest_day["day"]
        if hottest_day["max_temp"] not in (None, ""):
            max_bar = "+" * int(hottest_day["max_temp"])
        if hottest_day["min_temp"] not in (None, ""):
            min_bar = "+" * int(hottest_day["min_temp"])

    print(
        f"{day_str} {BLUE}{min_bar}{RESET}{RED}{max_bar}{RESET}{int(hottest_day['min_temp'])}C-{int(hottest_day['max_temp'])}C"
    )

    # bars for coldest day
    if coldest_day:
        day_str = coldest_day["day"]
        if coldest_day["max_temp"] not in (None, ""):
            max_bar = "+" * int(coldest_day["max_temp"])
        if coldest_day["min_temp"] not in (None, ""):
            min_bar = "+" * int(coldest_day["min_temp"])
    print(
        f"{day_str} {BLUE}{min_bar}{RESET}{RED}{max_bar}{RESET}{int(coldest_day['min_temp'])}C-{int(coldest_day['max_temp'])}C"
    )
