import csv, os
values = []
with open("C:/Users/Rajeev Dubey/Desktop/Solution/Input/main.csv",'rt') as f:
    data = csv.reader(f)
    for row in data:
        values.append(row)
header = values[0]
values = values[1:]

with open('C:/Users/rajeev Dubey/Desktop/Solution/Output/filteredCountrye.csv', 'w') as file:
    writer = csv.writer(file, delimiter = ',' , quotechar='"', quoting =csv.QUOTE_MINIMAL)
    writer.writerow(header)
    for rows in values:
        if 'USA' in rows[-1]:
            writer.writerow(rows)























