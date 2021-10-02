import sys

from config import Config


def parse_args(args):
    config = Config()
    return config


def main(args):
    config = parse_args(args)


if __name__ == '__main__':
    main(sys.argv[1:])
