import csv 
file = "data.csv"
with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    for index,column in enumerate(header):
        print(f"Column {index}: {column}")