from utils import month_names


def find_extreme_values(all_records, target_year):

    year_records = []
    for r in all_records:
        if r["year"] == target_year:
            year_records.append(r)

    if not year_records:
        print("No data found for year", target_year)
        return

    highest_temp_record = None
    lowest_temp_record = None
    humid_record = None

    for r in year_records:
        if r["max_temp"] is not None:
            if (
                highest_temp_record is None
                or r["max_temp"] > highest_temp_record["max_temp"]
            ):
                highest_temp_record = r

        if r["min_temp"] is not None:
            if (
                lowest_temp_record is None
                or r["min_temp"] < lowest_temp_record["min_temp"]
            ):
                lowest_temp_record = r

        if r["humidity"] is not None:
            if humid_record is None or r["humidity"] > humid_record["humidity"]:
                humid_record = r

    if highest_temp_record:
        print(
            f"Highest: {int(highest_temp_record['max_temp'])}C on {month_names[highest_temp_record['month']]} {highest_temp_record['day']}"
        )

    if lowest_temp_record:
        print(
            f"Lowest: {int(lowest_temp_record['min_temp'])}C on {month_names[lowest_temp_record['month']]} {lowest_temp_record['day']}"
        )

    if humid_record:
        print(
            f"Humid: {int(humid_record['humidity'])}% on {month_names[humid_record['month']]} {humid_record['day']}"
        )


def calculate_averages(all_records, target_year, target_month):

    month_records = []
    for r in all_records:
        if r["year"] == target_year and r["month"] == target_month:
            month_records.append(r)

    if not month_records:
        print("No data found for", target_year, "/", target_month)
        return

    max_temps = []
    min_temps = []
    humidities = []

    for r in month_records:
        if r["max_temp"] is not None and r["max_temp"] != "":
            max_temps.append(r["max_temp"])
        if r["min_temp"] is not None and r["min_temp"] != "":
            min_temps.append(r["min_temp"])
        if r["humidity"] is not None and r["humidity"] != "":
            humidities.append(r["humidity"])

    if max_temps:
        highest_avg = sum(max_temps) / len(max_temps)
        print("Highest Average:", int(highest_avg), "C")

    if min_temps:
        lowest_avg = sum(min_temps) / len(min_temps)
        print("Lowest Average:", int(lowest_avg), "C")

    if humidities:
        avg_humidity = sum(humidities) / len(humidities)
        print("Average Humidity:", int(avg_humidity), "%")
