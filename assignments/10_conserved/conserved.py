#!/usr/bin/env python3
"""
Author: Julia Misemer
Purpose: Show conserved bases in aligned sequences
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description='Show conserved bases in aligned sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main function"""

    args = get_args()
    filename = args.file

    if not os.path.isfile(filename):
        sys.exit(f"No such file or directory: '{filename}'")

    with open(filename) as fh:
        sequences = [line.strip() for line in fh if line.strip()]

    for seq in sequences:
        print(seq)

    print(get_conserved_line(sequences))


# --------------------------------------------------
def get_conserved_line(sequences):
    """Return a string showing conserved positions"""

    return ''.join(
        '|' if all(base == bases[0] for base in bases) else 'X'
        for bases in zip(*sequences)
    )


# --------------------------------------------------
if __name__ == '__main__':
    main()
