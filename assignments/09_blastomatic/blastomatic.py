#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-05-03
Purpose: Parse delimited text files
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Parse delimited text files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)



    parser.add_argument('-b',
                        '--blasthits',
                        help='BLAST -outfmt 6',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-a',
                        '--annotations',
                        help='Annotations file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-d',
                        '--delimiter',
                        help='Output field delimiter',
                        metavar='str',
                        type=str,
                        default=''
                        )
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',

                        type=argparse.FileType('wt'),
                        default='out.csv'
                        )
                    
    parser.add_argument('-p',
                        '--pctid',
                        help='Minimum percent',
                        metavar='float',
                        type=float,
                        default=0.0
                        )

    parser.add_argument('-f',
                        '--on',
                        help='A boolean flag',
                        action='store_true'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""


    args = get_args()
    file_arg = args.blasthits
    file_arg = args.annotations
    str_arg = args.delimiter
    file_arg = args.outfile
    int_arg = args.pctid
    flag_arg = args.on
    pos_arg = args.positional


    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')











# --------------------------------------------------
if __name__ == '__main__':
    main()
