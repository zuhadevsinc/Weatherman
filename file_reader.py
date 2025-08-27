import os


def read_all_weather_files(folder_path):
    all_weather_records = []
    files = os.listdir(folder_path)

    for filename in files:
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # print(f"Reading file: {file_path}")

            with open(file_path, "r") as file:
                lines = file.readlines()

                for line in lines[1:]:
                    parts = line.split(",")
                    try:
                        date = parts[0]  # "2006-6-1"
                        date_parts = date.split("-")
                        year = int(date_parts[0])
                        month = int(date_parts[1])
                        day = int(date_parts[2])

                        max_temp = parts[1]
                        min_temp = parts[3]
                        max_humidity = parts[7]

                        # print(date, max_temp, min_temp, max_humidity)

                        # Converting empty strings to None to avoid invalid data
                        if max_temp != "":
                            max_temp = float(max_temp)
                        else:
                            max_temp = None

                        if min_temp != "":
                            min_temp = float(min_temp)
                        else:
                            min_temp = None

                        if max_humidity != "":
                            max_humidity = float(max_humidity)
                        else:
                            max_humidity = None

                        # Creating a weather record (dictionary)
                        weather_record = {
                            "year": year,
                            "month": month,
                            "day": day,
                            "date": date,
                            "max_temp": max_temp,
                            "min_temp": min_temp,
                            "humidity": max_humidity,
                        }

                        all_weather_records.append(weather_record)

                    except:
                        continue
    return all_weather_records
