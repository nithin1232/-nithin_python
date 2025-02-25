### (1) read the csv file Python-Learning/files/Data.csv
### (2) Check "Room Temp" and "Device Temp" are with 5% threshold
### (3) Value1 will increase when temp cross 55 +/-5%
### (4) Value2 and Value6 should increase after every 15 +/-5% deg change in temp
### (5) Value3, Value4, Value5 should increase after every 25 +/-5% dev change in temp.


import csv

file_path = 'C:\\Users\\Nithon\\Python-Learning\\files\\data.csv'
threshold = 0.05


with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row[0:2])






















