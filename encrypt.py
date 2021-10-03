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


def option_w(index, args, config):
    if len(args[index]) == 2 and index < len(args) - 1 and type(args[index + 1]) == str:
        config.set_width(args[index + 1])
    return True


def option_C(index, args, config):
    config.set_force_complete(True)
    return False


def option_k(index, args, config):
    if len(args[index]) == 2 and index < len(args) - 1 and type(args[index + 1]) == str:
        config.append_keyword(args[index + 1])
    return True


def option_R(index, args, config):
    config.set_rearrange(True)
    return False


def option_i(index, args, config):
    if len(args[index]) == 2 and index < len(args) - 1 and type(args[index + 1]) == int:
        config.set_iterations(args[index + 1])
    return True


def option_h():
    print_help()
    sys.exit(0)


def parse_args(args):
    config = Config()
    value_read = False
    opcodes = {
        "w": option_w,
        "h": option_h,
        "C": option_C,
        "k": option_k,
        "R": option_R,
        "i": option_i
    }
    for index, arg in enumerate(args):
        if arg[0] == "-":
            for option in arg[1:]:
                if option in opcodes.keys():
                    value_read = opcodes[option](index, args, config)
        elif value_read:
            value_read = False
        else:
            if index == len(args) - 1:
                config.set_infile_name(arg)
    return config


def main(args):
    config = parse_args(args)


if __name__ == '__main__':
    main(sys.argv[1:])
