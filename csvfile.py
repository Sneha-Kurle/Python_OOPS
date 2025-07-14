import json
import csv
data=[['num','name','Age'],
      [1, 'sneha', 25],
      [2, 'aishu',27],
      [3,'aayi',55]]
file_path= "C:\\Users\\sneha\\OneDrive\\Desktop\\page.csv"
with open(file_path, 'w', newline='') as file:
    writer=csv.writer(file)
    for i in data:
        writer.writerow(i)
    print(('the csv file is exist and the data has inserted'))

