#!/usr/bin/env python3
"""
Author : Julia Misemer <jkmisemer@arizona.edu>
Date   : 2025-05-07
Purpose: Run-length encoding of DNA sequences
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Run-length encode a sequence"""
    if not seq:
        return ''
    result = []
    prev = seq[0]
    count = 1
    for base in seq[1:]:
        if base == prev:
            count += 1
        else:
            result.append(prev + (str(count) if count > 1 else ''))
            prev = base
            count = 1
    result.append(prev + (str(count) if count > 1 else ''))
    return ''.join(result)


# --------------------------------------------------
def main():
    """Main logic for run-length encoding"""

    args = get_args()
    input_str = args.str

    # Determine if input is a file path or sequence
    if os.path.isfile(input_str):
        with open(input_str) as fh:
            lines = fh.read().splitlines()
    else:
        lines = [input_str]

    for line in lines:
        print(rle(line))


# --------------------------------------------------
def test_rle():
    """Unit tests for the rle function"""
    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
