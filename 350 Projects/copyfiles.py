#!/usr/bin/env python3
"""
This module copies all files with a given extension in a given directory
into a subdirectory having the same name as the directory.
"""

import sys
import os
import glob
import shutil

__author__ = 'Sergio Sum Munoz'


def main():
    """
    Copies all files with a given extension in a given directory
    into a subdirectory having the same name as the directory.
    The directory is specified in the first command line argument.
    The file name extension is specified in the second command line
    argument.

    :return: 0 if executes successfully,
             1 if two command line args are not supplied,
             2 if the first command line arg is not a directory,
             3 if no files in the directory have the extension,
             4 if a subdirectory of the given directory has the
               same name and therefore cannot be created.
    """

    # The program must detect some errors:
    # Exactly two command line arguments are not supplied
    args = sys.argv
    if len(args) != 3:
        print("Usage: {} <dir-path> <extension>".format(args[0]),
              file=sys.stderr)
        return 1

    # Name the two command line arguments
    dir_path = args[1]
    filename_ext = args[2]

    print('Processing {} files in directory "{}"'.format(filename_ext, dir_path))

    # Algorithm


    # 2. dir_path does not exist
    if not os.path.isdir(dir_path):
        print('{} is not a directory'.format(dir_path), file=sys.stderr)
        return 2

    # 3. No file in dir_path has extension filename_ext
    os.chdir(dir_path)
    matching_filenames = glob.glob('*'+ filename_ext)
    if matching_filenames == []:
        print("There are no file names with that extension")
        return 3

    # 4. D already has a subdirectory with the same nam
    head, sub_dir = os.path.split(dir_path)
    if os.path.isdir(sub_dir):
        print('There is already a subdirectory with the same name')
        return 4

    # Create a subfolder (subdirectory) having name D.
    os.mkdir(sub_dir)

    # Find all of the files in D having extension E.


    # Copy each of the files to the subdirectory.
    for file_name in matching_filenames:
        shutil.copy(file_name, sub_dir)

    # --Zip the subdirectory
    # --Remove the subdirectory and its contents
    #
    # Notes
    # Steps 4 and 5 are not needed.
    # D and E are provided to the program as command line arguments.


    return 0


if __name__ == '__main__':
    main()