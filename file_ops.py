"""

+----------------+--------------------------------------------------------------+
| Author:        | Ganesh Kuramsetti                                            |
+----------------+--------------------------------------------------------------+
| Script Name:   | file_ops.py                                                  |
+----------------+--------------------------------------------------------------+
| Date Created:  | 12-Jun-2021                                                  |
+----------------+--------------------------------------------------------------+
| Description:   | A module file that holds all the predefined file operations. |
+----------------+--------------------------------------------------------------+
| Language:      | Python                                                       |
+----------------+--------------------------------------------------------------+
| Prerequisites: | Python3                                                      |
+----------------+--------------------------------------------------------------+
| Instructions:  | Do not execute this file, import and use instead.            |
+----------------+--------------------------------------------------------------+
| Date Updated:  | 07-July-2022                                                 +
+----------------+--------------------------------------------------------------+

"""

# !/usr/bin/python

# importing libraries.
import difflib
import os
import hashlib
import json
from .log_ops import log_with_pre_bffr


def read_file_data(file_path):
    """
    Reads and return data from the given file path.
    An empty string will be returned if path doesn't exist or in case of any exception.
    """
    file_data = ""
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file_to_read:
                file_data = file_to_read.readlines()
            return file_data
        except OSError:
            log_with_pre_bffr(f"Some error occurred while reading the file at {file_path}.")
            return file_data
    else:
        log_with_pre_bffr(f"File path {file_path} doesn't exist.")
        return file_data


def calculate_file_checksum(file_path):
    """
    Determines checksum of file located at given file path
    """
    # Reading content of first file to calculate hash
    file_readability = read_file_data(file_path)
    if file_readability == "":
        log_with_pre_bffr(f"Cannot calculate checksum for file {file_path}.")
    else:
        with open(file_path, "rb") as req_file:
            # sha 256 hash
            checksum = hashlib.sha256()
            # md5 hash
            # checksum = hashlib.md5()
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: req_file.read(4096), b""):
                checksum.update(byte_block)
        # log_with_pre_bffr(f"Checksum for file {file_path} : {checksum.hexdigest()}.")
        return checksum.hexdigest()
    return None


def write_file_data(file_path: str, file_data: str):
    """
    writes data to a file in a given path.
    if files exists it will be over written.
    if file doesn't exists it will be created.
    """
    if os.path.exists(file_path):
        log_with_pre_bffr("File is avaialbe. Do you want to overwrite?(Y/N)")
        overwrite_file = input("Y or N : ")
        if overwrite_file == "Y":
            with open(file_path, "w") as file_to_write:
                file_to_write.write(file_data)
            log_with_pre_bffr(f"Data written to {file_path}.")
        else:
            with open(file_path, "a") as file_to_write:
                file_to_write.write(file_data)
            log_with_pre_bffr(f"Data appended to {file_path}.") 
    else:
        with open(file_path, "x") as file_to_write:
            file_to_write.write(file_data)
        log_with_pre_bffr(f"Created a new file {file_path} and data was written.")


def get_diff_btwn_two_files(first_file_path: str, second_file_path: str):
    """
    returns the difference between 2 files in a html format.
    """
    first_file_data = read_file_data(first_file_path)
    second_file_data = read_file_data(second_file_path)
    difference_data = ""
    if not(first_file_data == "" or second_file_data == ""):
        difference_data = difflib.HtmlDiff().make_file(
            first_file_data, second_file_data, "File: "+first_file_path, "File: "+second_file_path)
    return difference_data


def get_files_from_dir_and_its_sub_dir(dir_abs_path: str, excluded_sub_dirs: list):
    """
    This function returns all the files that are available in the given path
    and it's sub directories.
    You can also specify the directories that should be excluded from search.


    Args:
        dir_abs_path (string): 
        The absolute path of the search directory.
        excluded_sub_dirs (list): 
        The list of sub-directories that can be excluded from search.
        You can specify None if none of the sub-directories to be excluded.
        The list should contain just the name of sub-directory that should be excluded.

    Returns:
        list: Returns list of files in the given directory after exclusion. 
    """
    files_and_dirs = os.listdir(dir_abs_path)
    full_path_of_excluded_sub_dirs = list()
    # If none of the directories are specified initializing an empty list
    # If some directories specified initializing the list with the full path
    # of the directories
    if excluded_sub_dirs is None:
        excluded_sub_dirs = list()
    else:
        full_path_of_excluded_sub_dirs = []
        for an_ex_sub_dir in excluded_sub_dirs:
            full_path_of_excluded_sub_dirs.append(os.path.join(dir_abs_path, an_ex_sub_dir))
    all_files = list()
    for a_file_or_dir in files_and_dirs:
        full_path = os.path.join(dir_abs_path, a_file_or_dir)
        if os.path.isdir(full_path) and full_path not in full_path_of_excluded_sub_dirs:
            temp_files = get_files_from_dir_and_its_sub_dir(full_path, excluded_sub_dirs)
            for a_file in temp_files:
                all_files.append(a_file)
        elif os.path.isfile(full_path):
            all_files.append(full_path)
    return all_files


def compare_two_files(file1_path: str, file2_path: str):
    """
    Compares 2 files based on their checksum
    Returns 0 if both files are same.
    Returns 1 if both files are different.
    Returns -1 if one of the files checksum is undefined.

    Args:
        file1_path (str): Holds the full absolute path of first file.
        file2_path (str): Holds the full absolute path of second file.

    Returns:
        integer : returns 1, 0, or -1 based on the calculations.
    """
    # calculating the checksum of both the files
    first_file_checksum = calculate_file_checksum(file1_path)
    second_file_checksum = calculate_file_checksum(file2_path)
    # checksum comparison
    if not (first_file_checksum is None or second_file_checksum is None):
        if first_file_checksum != second_file_checksum:
            return 1          
        elif first_file_checksum == second_file_checksum:
            return 0
    else:
        return -1
        

def read_json_file_data(file_path: str):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file_to_read:
                file_data = json.load(file_to_read)
            return file_data
        except OSError:
            log_with_pre_bffr(f"Some error occurred while reading the json file at {file_path}.")
