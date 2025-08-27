import os
import sys
from file_reader import read_all_weather_files
from weather_analysis import find_extreme_values


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


if __name__ == "__main__":
    main()
