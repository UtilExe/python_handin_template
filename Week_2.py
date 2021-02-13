# Exercise 1

# 1. Create a python file with 3 functions:
# A. def print_file_content(file) that can print content of a csv file to the console
# B. def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
#      a. rewrite the function so that it gets an arbitrary number of strings instead of a list
# C. def read_csv(input_file) that take a csv file and read each row into a list

# A.: Print content of csv file to the console
# THROUGH WEB (webget download):
import argparse
import os
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


def print_file_content_2(path):
    with open(path) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))

# print_file_content_2('C:/Users/Emil/Desktop/Skole/Python/Materiale/tracking.csv');

# B.: def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file


def write_list_to_file(output_file, tupleL):
    with open(output_file, 'w') as file_object:
        for numb in tupleL:
            # "write() argument must be str, not int".. manually converting to str, in case it's numbers
            file_object.write(str(numb) + '\n')


tupleList = ('hello', 'there', 'how', 1, 6, 7, 9, 11)

write_list_to_file('C:/Users/Emil/Desktop/Skole/Python/Materiale/datamsg.txt', tupleList)

# B.a: rewrite the function so that it gets an arbitrary number of strings instead of a list


def write_list_to_file_arbitrary(output_file, *numbers):
    with open(output_file, 'w') as file_object:
        for numb in numbers:
            # "write() argument must be str, not int"next manually converting to str.
            file_object.write(str(numb) + '\n')

write_list_to_file_arbitrary('C:/Users/Emil/Desktop/Skole/Python/Materiale/datamsg2.txt', 'hello', 'there', 'how', 1, 6, 7, 9, 11, "new")


# C. def read_csv(input_file) that take a csv file and read each row into a list:
url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/cru/tas/year/CAN.csv'


def read_csv(input_file):
    with open(input_file) as f:
        rowList = []
        reader = csv.reader(f)
        # why it skips first row: https://www.kite.com/python/answers/how-to-skip-the-first-line-of-a-csv-file-in-python
        header_row = next(reader)

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


# with first Argument: python_handin_template/Week_2.py python_handin_template/datamsg.txt
# with two Arguments: python python_handin_template/Week_2.py python_handin_template/datamsg.txt -f python_handin_template/datawrite.txt -l word1 word2 word3
if __name__ == '__main__':
    """run with python Week_2.py input.txt -f output.txt -l word1 word2 word3"""
    parser = argparse.ArgumentParser(description='Solution to handin week 2')
    parser.add_argument('input_file', help='the input file to consume')
    # nargs='*' means 0 or more args, nargs='+' means 1 or more
    parser.add_argument('-l', '--list', nargs='*',
                        help='extra words', required=False)
    parser.add_argument('-f', '--output_file',
                        help='the file to print to. (console if nothing is given)')

    args = parser.parse_args()
   # print('INPUT:', args.input_file)
   # print('File:', args.output_file)
  #  print('List:', args.list)
  #  print('Len', vars(args))

    # only first arg. usage: python_handin_template/Week_2.py python_handin_template/datamsg.txt
    if not (args.output_file and args.list):
        print_file_content_2(args.input_file)
    # only input and output. usage: python python_handin_template/Week_2.py python_handin_template/datamsg.txt -f python_handin_template/datawrite.txt -l word1 word2 word3
    else:
        lst = print_file_content_2(args.input_file)
         # not sure why the commented lines were necessary in Thomas' sample file. Seems to work without.
         # if args.list:
         #   lst.extend(args.list)
         # print('LISTEN:',lst)
        write_list_to_file(args.output_file, args.list)
