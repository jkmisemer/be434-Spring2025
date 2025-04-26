#!/usr/bin/env python3
"""
Author : Your Name <your_email@example.com>
Date   : 2025-04-26
Purpose: Compute GC content
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='?',
                        type=argparse.FileType('rt'),
                        default=sys.stdin,
                        help='Input sequence file (default: stdin)')

    return parser.parse_args()

# --------------------------------------------------
def read_fasta(fh):
    """Read a FASTA file"""

    seq_id = None
    seq = []

    for line in fh:
        line = line.strip()
        if line.startswith('>'):
            if seq_id:
                yield (seq_id, ''.join(seq))
            seq_id = line[1:]
            seq = []
        else:
            seq.append(line)
    if seq_id:
        yield (seq_id, ''.join(seq))

# --------------------------------------------------
def gc_content(seq):
    """Calculate GC content percentage"""

    gc_count = sum(1 for base in seq if base in 'GCgc')
    return (gc_count / len(seq)) * 100 if seq else 0

# --------------------------------------------------
def main():
    """Compute GC content"""

    args = get_args()
    filehandle = args.file

    max_id = None
    max_gc = 0

    for seq_id, seq in read_fasta(filehandle):
        gc = gc_content(seq)
        if gc > max_gc:
            max_gc = gc
            max_id = seq_id

    if max_id:
        print(f'{max_id} {max_gc:.6f}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
