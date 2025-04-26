#!/usr/bin/env python3
"""
Author : Julia <Add your email>
Date   : 2025-04-24
Purpose: Divide some numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Divide some numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='str',
                        nargs=2,
                        type=int,
                        help='Numbers to divide')

    args = parser.parse_args()
    if args.numbers[1] == 0:
        parser.error(f"Cannot divide by zero, dum-dum!")
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.numbers
    n1=numbers[0]
    n2=numbers[1]
    result = int(n1/n2)
    print(f'{n1} / {n2} = {result}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
