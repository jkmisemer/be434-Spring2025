#!/usr/bin/env python3
"""
Author : Julia Misemer <jkmisemer@arizona.edu>
Date   : 2025-04-26
Purpose: Transcribe DNA into RNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
    parser.add_argument('FILE',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input DNA file(s)')

    
    parser.add_argument('-o', '--out_dir',
                        metavar='DIR',
                        default='out',
                        help='Output directory (default: out)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Transcribe DNA into RNA"""
    args = get_args()

    out_dir = args.out_dir
    os.makedirs(out_dir, exist_ok=True)

    num_seqs = 0
    num_files = 0

    
    for file_handle in args.FILE:
        lines = [line.strip().replace('T', 'U') for line in file_handle if line.strip()]
        out_file = os.path.join(out_dir, os.path.basename(file_handle.name))
        with open(out_file, 'w') as f:
            f.write('\n'.join(lines) + '\n')

        num_seqs += len(lines)
        num_files += 1

    
    print(f'Done, wrote {num_seqs} sequence{"s"*(num_seqs!=1)} '
          f'in {num_files} file{"s"*(num_files!=1)} to directory "{out_dir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
