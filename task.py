import os
import sys
from file_reader import read_all_weather_files


def main():

    # python3 task.py -e 2006 ./Murree_weather

    option = sys.argv[1]  # -e, -a, or -c
    date_input = sys.argv[2]  # year or year/month
    folder_path = sys.argv[3]  # path to files

    print("Reading weather files...")
    all_records = read_all_weather_files(folder_path)
    print(f"Found {len(all_records)} weather records")
    print()


if __name__ == "__main__":
    main()
