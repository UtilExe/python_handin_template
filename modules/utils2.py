import os
def get_file_names(folderpath, out='file_data/output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    entries = os.listdir(folderpath)
    
    with open(out, 'w') as file_object:
        for entry in entries:
            file_object.write(str(entry) + '\n')
    
def get_all_file_names(folderpath,out='file_data/output2.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

    with open(out, 'w') as file_object:
        for root, dirs, files in os.walk(folderpath):
            for name in files:
                file_object.write(str(name) + '\n')

# not sure if this is the right way. using the * abritary function parameter. not sure if there's a smarter way?
def print_line_one(*file_names):
    """takes a list of filenames and print the first line of each"""
    lines = []
    for file in file_names:
        with open(file) as file_object:
            lines.append("File: " + file +": " + file_object.readline()) #readline handles to read only first line
    
    for line in lines:
        print(line.rstrip())

# not sure if this is the right way. using the * abritary function parameter. not sure if there's a smarter way?
def print_emails(*file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    lines = []
    for file in file_names:
        with open(file) as file_object:
            line = file_object.readlines();
            for entry in line:
                if ('@' in entry):
                    lines.append("File: " + file +": " + entry)

    for line in lines:
        print(line.rstrip())

def write_headlines(*md_files, out='file_data/output3.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    lines = []
    for file in md_files:
        with open(file) as file_object:
            line = file_object.readlines();
            for entry in line:
                if ('#' in entry):
                    lines.append("File: " + file +": " + entry)
        with open(out, 'w') as file_object:
            for field in lines:
               # print("test", field)
                file_object.write(str(field))