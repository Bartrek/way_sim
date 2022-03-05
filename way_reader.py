import os
import getopt
import sys

def get_parameters():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print(f'Usage: {os.path.split(sys.argv[0])[1]} -i <inputfile> ')
        sys.exit(2)

    print(opts)
    print(args)

    if not opts:
        print(f'Usage: {os.path.split(sys.argv[0])[1]} -i <inputfile> ')
        sys.exit(2)

    return opts



if __name__ == '__main__':
    print(get_parameters())
    print('dupa')

