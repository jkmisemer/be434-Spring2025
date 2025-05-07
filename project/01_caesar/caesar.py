#!/usr/bin/env python3
"""
Author : Your Name
Date   : 2025-05-07
Purpose: Encode or decode Caesar cipher from a file
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Caesar cipher encoder/decoder',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file to encode/decode')

    parser.add_argument('-n',
                        '--shift',
                        metavar='int',
                        type=int,
                        default=3,
                        help='Shift amount (default: 3)')

    parser.add_argument('--decode',
                        action='store_true',
                        help='Decode the input')

    return parser.parse_args()


# --------------------------------------------------
def shift_char(c: str, shift: int) -> str:
    """Shift a single character preserving case"""

    if c.isalpha():
        base = ord('A') if c.isupper() else ord('a')
        return chr((ord(c) - base + shift) % 26 + base)
    return c


# --------------------------------------------------
def shift_text(text: str, shift: int, decode: bool = False) -> str:
    """Shift entire string, returning UPPERCASE result"""

    if decode:
        shift = -shift

    shifted = ''.join(shift_char(c, shift) for c in text)
    return shifted.upper()


# --------------------------------------------------
def main():
    """Main function"""

    args = get_args()

    if not os.path.isfile(args.file):
        sys.exit(f"usage: caesar.py [-h] [-n int] [--decode] FILE\ncaesar.py: error: No such file or directory: '{args.file}'")

    with open(args.file, 'rt') as fh:
        contents = fh.read()

    output = shift_text(contents, args.shift, args.decode)
    print(output, end='')  


# --------------------------------------------------
if __name__ == '__main__':
    main()
