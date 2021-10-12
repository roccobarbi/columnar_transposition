import random
import string
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


def option_C(index, args, config):  # TODO: use this
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


def option_h(index, args, config):
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
            else:
                print("Wrong arguments!")
                print_help()
    return config


def read_infile(config):
    plain_text = ""
    with open(config.infile_name, "r") as infile:
        for line in infile:
            plain_text += ''.join(line.rstrip("\n").split())
    return plain_text


def encipher(current_text, keyword, config):
    """
    encipher takes the current text, the keyword and the configuration object and it returns the ciphertext

    Assumptions on input: the current text and the keyword may be in any case, without whitespace
    Preprocessing: the text and the keyword will be converted to uppercase before usage
    Assumptions on output: the output will always be uppercase

    :param current_text:
    :param keyword:
    :param config:
    :return:
    """
    columns = []
    cypher_text = ""
    width = len(keyword)
    keyword = keyword.upper()
    current_text = current_text.upper()
    for index in range(width):
        columns.append("")
    for position, character in enumerate(current_text):
        columns[position % width] += character
    if config.rearrange:  # Inefficient at scale, but this is a first MVP
        for current_letter in string.ascii_uppercase:
            for index, letter in enumerate(keyword):
                if letter == current_letter:
                    cypher_text += columns[index]
    else:
        for column in columns:
            cypher_text += column
    return cypher_text


def add_padding(current_text, length):
    padding = ""
    for missing in range(length):
        padding += random.choice(string.ascii_letters)
    return current_text + padding


def main(args):
    config = parse_args(args)
    current_text = read_infile(config)
    for iteration in range(config.iterations):
        if config.keywords is not None:
            if len(config.keywords) <= iteration + 1:
                keyword = config.keywords[iteration - 1]
            else:
                keyword = config.keywords[-1]
        else:  # Use the width as a fallback
            keyword = str(range(config.width))
        if config.force_complete and len(current_text) % len(keyword) != 0:
            current_text = add_padding(current_text, len(keyword) - (len(current_text) % len(keyword)))
        current_text = encipher(current_text, keyword, config)
    print(current_text)


if __name__ == '__main__':
    main(sys.argv[1:])
