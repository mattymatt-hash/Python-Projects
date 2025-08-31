import csv

# Use the full path and raw string to avoid issues with backslashes
file_path = r"C:\mathewstevens.info\cis189python\module_13\example CSV(1).csv"

with open(file_path, newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
