# file_path= 'C:\\Users\\sneha\\OneDrive\\Desktop\\page.txt'
# try:
#     with open(file_path,'r') as file:
#         content=file.read()
#         print(content)
# except FileNotFoundError:
#     print('file not found')

#Json file reading
# import json
# file_path= 'C:\\Users\\sneha\\OneDrive\\Desktop\\file.json'
# try:
#     with open(file_path,'r') as file:
#         content=json.load(file)
#         print(content)
# except FileNotFoundError:
#     print('file not found')

#csv file reading>>
import csv
file_path= 'C:\\Users\\sneha\\OneDrive\\Desktop\\page.csv'
try:
    with open(file_path,'r') as file:
        content=csv.reader(file)
        for i in content:
            print(i)
except FileNotFoundError:
    print('file not found')