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


# Gemini generated code :
"""
from datetime import datetime
import csv

file = "people-100.csv"
with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    values = []
    for row in reader:
        # 'date' is already a datetime object
        date = datetime.strptime(row[7],'%Y-%m-%d')
        values.append(date)

# Now, let's demonstrate how to display them differently
print("Original datetime objects:")
print(values[0]) # Example of the first element in its raw datetime object form
print(values[1])

print("\nDates formatted as 'YYYY-MM-DD':")
for dt_obj in values[:5]: # Displaying the first 5 for brevity
    print(dt_obj.strftime('%Y-%m-%d'))

print("\nDates formatted as 'DD/MM/YYYY':")
for dt_obj in values[:5]:
    print(dt_obj.strftime('%d/%m/%Y'))

print("\nDates formatted with full month name and weekday:")
for dt_obj in values[:5]:
    print(dt_obj.strftime('%A, %d %B %Y'))
# The code above reads a CSV file, extracts the 'Date of Birth' column,
# converts it to datetime objects, and then formats and prints the dates in various formats."""
