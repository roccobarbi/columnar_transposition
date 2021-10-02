import sys

from config import Config


def print_help():
    print("encrypt with a columnar transposition cypher")
    print("")
    print("Usage:")
    print("    python3 encrypt.py -w {width} [OPTIONS] {input filename or path}")
    print("")
    print("OPTIONS:")
    print("-w Followed by a positive integer, the width of the table used to encrypt the plaintext.")
    print("-C Forces a complete columnar transposition, random characters will be used for padding.")
    print("-k Followed by a keyword (keywords are used in the order they are written, excess ones will be ignored).")
    print("-R The columns will be read in the alphabetical order of the key (left to right in case of ties).")
    print("-i Followed by a positive integer, the number of iterations used (default 1). If too few keywords are" +
          "   provided, the last one is used again as many times as needed.")
    print("-h Print this message and quit.")


def parse_args(args):
    config = Config()
    for arg in args:
        if arg[0] == "-h":
            print_help()
    return config


def main(args):
    config = parse_args(args)


if __name__ == '__main__':
    main(sys.argv[1:])
