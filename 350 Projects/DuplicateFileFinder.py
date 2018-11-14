import sys
import os


__author__ = 'Sergio Sum Munoz'



def magic(directory):
    file_dictionary = {}

    for dir_path, dir_name, file_name in os.walk(directory):
        for file in file_name:
            file_path = os.path.join(dir_path, file)
            file_size = os.path.getsize(file_path)
            print(file, file_size, file_path)
            key_tup = (file, file_size)

            if key_tup not in file_dictionary:
                file_dictionary[key_tup] = [file_path]
                print(file_dictionary)

            else:
                print('This tuple is already a key, it must be the same file in a different location.')
                file_dictionary[key_tup].append(file_path)
                print(file_dictionary)





    # return(file_dictionary)

    # for k, v1 in file_dictionary.items():
    #         print(k, v1)

def main():
    # The program must detect some errors:
    # Exactly two command line arguments are not supplied
    args = sys.argv
    if len(args) == 1:
        print("Usage: {} <dir-path>".format(args[0]), file=sys.stderr)
        sys.exit(1)


    # Name the command line argument
    directory = args[1]

    #print('Processing {} files in directory "{}"'.format(directory))

    # dir_path does not exist
    if not os.path.isdir(directory):
        print('{} is not a directory'.format(directory), file=sys.stderr)
        sys.exit(2)

    print(magic(directory))


if __name__ == '__main__':
    main()