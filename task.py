import os
import sys
from file_reader import read_all_weather_files
from weather_analysis import find_extreme_values, calculate_averages
from charts import draw_charts, draw_combined_charts


def main():

    # python3 task.py -e 2006 ./Murree_weather

    option = sys.argv[1]  # -e, -a, or -c
    date_input = sys.argv[2]  # year or year/month
    folder_path = sys.argv[3]  # path to files

    print("Reading weather files...")
    all_records = read_all_weather_files(folder_path)
    print(f"Found {len(all_records)} weather records")

    # Extreme values
    if option == "-e":
        year = int(date_input)
        find_extreme_values(all_records, year)
    elif option == "-a":

        year_month = date_input.split("/")
        year = int(year_month[0])
        month = int(year_month[1])
        calculate_averages(all_records, year, month)
    elif option == "-c":
        # Charts for a month
        year_month = date_input.split("/")
        year = int(year_month[0])
        month = int(year_month[1])

        # draw_charts(all_records, year, month)
        draw_combined_charts(all_records, year, month)

    else:
        print("Invalid option. Use -e for extreme values or -a for averages.")


if __name__ == "__main__":
    main()
