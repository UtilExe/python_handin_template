# Exercise 1

# 1. Create a python file with 3 functions:
# A. def print_file_content(file) that can print content of a csv file to the console
# B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
#      a. rewrite the function so that it gets an arbitrary number of strings instead of a list
# C. def read_csv(input_file) that take a csv file and read each row into a list

# A.: Print content of csv file to the console
## THROUGH WEB (webget download):
from modules import webget
import csv

# Self-note: We process them through the csv libray, isntead of the string techniques we learend earlier in Working_With_Files
url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv'
def print_file_content():
    webget.download(url)

    with open('CAN.csv') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))
      
print_file_content()

# THROUGH file on PC (note: the file contains different csv content/data):
import os
def print_file_content_2(path):
    with open(path) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))

###print_file_content_2('C:/Users/Emil/Desktop/Skole/Python/Materiale/tracking.csv');

# B.: def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
def write_list_to_file(output_file, tupleL):
    with open(output_file, 'w') as file_object:
        for numb in tupleL: 
            file_object.write(str(numb) + '\n') ### "write() argument must be str, not int".. manually converting to str, in case it's numbers

tupleList = ('hello', 'there', 'how', 1, 6, 7, 9, 11)

write_list_to_file('C:/Users/Emil/Desktop/Skole/Python/Materiale/datamsg.txt', tupleList)

# B.a: rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list_to_file_arbitrary(output_file, *numbers):
    with open(output_file, 'w') as file_object:
        for numb in numbers: 
            file_object.write(str(numb) + '\n') ### "write() argument must be str, not int".. manually converting to str. 

write_list_to_file_arbitrary('C:/Users/Emil/Desktop/Skole/Python/Materiale/datamsg2.txt', 'hello', 'there', 'how', 1, 6, 7, 9, 11, "new")

# C. def read_csv(input_file) that take a csv file and read each row into a list:
url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv'
def read_csv(input_file):
    with open(input_file) as f:
        rowList = []
        reader = csv.reader(f)
        header_row = next(reader) # why it skips first row: https://www.kite.com/python/answers/how-to-skip-the-first-line-of-a-csv-file-in-python

        for row in reader:
            # add to the new list
            rowList.append(row)
    # contains one combined list.
    for items in rowList:
        print(items)
 #   print(rowList)

read_csv('C:/Users/Emil/Desktop/Skole/Python/Materiale/data.csv');

# 2. Add a functionality so that the file can be called from cli with 2 arguments
# 2.A path to csv file
# 2.B an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.

# 3. Add a --help cli argument to describe how the module is used
