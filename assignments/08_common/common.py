#!/usr/bin/env python3
"""
Author : Julia Misemer <jkmisemer@arizona.edu>
Date   : 2025-04-27
Purpose: Find common words in two files
"""
# --------------------------------------------------
import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1', help='Input file 1')
    parser.add_argument('file2', help='Input file 2')
    parser.add_argument('-o', '--outfile', help='Output file', type=str)

    return parser.parse_args()


# --------------------------------------------------
def get_words(filehandle):
    """Extract all words from a filehandle"""

    words = set()
    for line in filehandle:
        words.update(line.split())
    return words


# --------------------------------------------------
def main():
    """Main program logic"""

    args = get_args()

    for filename in [args.file1, args.file2]:
        if not os.path.isfile(filename):
            sys.exit(f"No such file or directory: '{filename}'")

    with open(args.file1, 'rt', encoding='utf-8') as fh1, open(args.file2, 'rt', encoding='utf-8') as fh2:
        words1 = get_words(fh1)
        words2 = get_words(fh2)

    common_words = sorted(words1 & words2)

    if args.outfile:
        with open(args.outfile, 'wt', encoding='utf-8') as out_fh:
            for word in common_words:
                print(word, file=out_fh)
    else:
        for word in common_words:
            print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()