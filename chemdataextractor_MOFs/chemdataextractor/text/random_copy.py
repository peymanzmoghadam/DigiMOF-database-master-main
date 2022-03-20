import os
import shutil
import random

input_dir = 'C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\Performance Corpus'
output_dir = 'C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\Test Corpus'
def get_file_list(input_dir):
    return [file for file in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, file))]

def get_random_files(file_list, N):
    return random.sample(file_list, N)

def copy_files(random_files, input_dir, output_dir):
    for file in random_files:
        shutil.copy(os.path.join(input_dir, file), output_dir)

def main(input_dir, output_dir, N):
    file_list = get_file_list(input_dir)
    random_files = get_random_files(file_list, 50)
    copy_files(random_files, input_dir, output_dir)

main(input_dir, output_dir, 50)