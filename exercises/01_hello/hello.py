#!/usr/bin/env python3
"""
Author : Julia
Date   : 2025-02-05
Purpose: say hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

                                   
    parser.add_argument('-n',
                        '--name',
                        help='A name to greet',
                        metavar='str',
                        type=str,
                        default='World')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    name = args.name
    print(f'Hello, {name}!')
                    


# --------------------------------------------------
if __name__ == '__main__':
    main()
