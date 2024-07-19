import csv

with open("advertising.csv") as file:
    file_csv = csv.reader(file,delimiter=",")

    for i,line in enumerate(file_csv):
        if i == 1:
            print("Head: " + str(line))
        else:
            print("Value: " + str(line))