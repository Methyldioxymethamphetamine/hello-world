from datetime import datetime
import csv

file = "people-100.csv"
with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    # Renamed 'values' to 'dates_of_birth' for clarity
    dates_of_birth = []
    for row in reader:
        # Assuming row[7] is indeed the 'Date of Birth' column
        date_of_birth = datetime.strptime(row[7],'%Y-%m-%d')
        dates_of_birth.append(date_of_birth)


for dt in dates_of_birth[:5]: # Displaying the first 5 for brevity
    print(dt.strftime('%Y-%m-%d'))
