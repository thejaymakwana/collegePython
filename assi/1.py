
import csv
with open('college.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # print(data)    
    for row in data:
        print(', '.join(row))
csvfile.close()