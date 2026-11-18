import csv
#open the csv file in the read mode
with open(r"students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)