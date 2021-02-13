import os
def get_file_names(folderpath, out='python_handin_template/output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    entries = os.listdir(folderpath)
    
    with open(out, 'w') as file_object:
        for entry in entries:
            file_object.write(str(entry) + '\n')
    
def get_all_file_names(folderpath,out='python_handin_template/output2.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""

    with open(out, 'w') as file_object:
        for root, dirs, files in os.walk(folderpath):
            for name in files:
                file_object.write(str(name) + '\n')

def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""

def write_headlines(md_files, out='output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""