import csv

with open("SampleDataupdate.csv", "r") as file:
    reader = csv.DictReader(file)
      # next(reader) hack to skip the first Row
    for row in reader:
        print(row["Rep"])
