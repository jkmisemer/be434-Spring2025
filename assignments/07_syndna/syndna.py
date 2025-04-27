#!/usr/bin/env python3
"""
Author : Julia Misemer <jkmisemer@arizona.edu>
Date   : 2025-04-26
Purpose: create synthetic DNA/RNA sequences
"""

import argparse
import random
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Generate synthetic DNA/RNA sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum sequence length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum sequence length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-t',
                        '--seqtype',
                        help='Sequence type (dna or rna)',
                        metavar='str',
                        type=str,
                        default='dna',
                        choices=['dna', 'rna'])

    parser.add_argument('-p',
                        '--pctgc',
                        help='Desired GC content (0-1)',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='out.fa')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    if args.minlen < 1 or args.maxlen < args.minlen:
        parser.error('Minimum length must be > 0 and <= maximum length')

    if args.numseqs < 1:
        parser.error('Number of sequences must be > 0')

    return args

# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    random.seed(args.seed)

    gc_bases = ('G', 'C')
    at_bases = ('A', 'T') if args.seqtype == 'dna' else ('A', 'U')

    with open(args.outfile, 'wt') as fh:
        for i in range(1, args.numseqs + 1):
            length = random.randint(args.minlen, args.maxlen)
            seq = []
            for _ in range(length):
                base = random.choice(gc_bases) if random.random() < args.pctgc else random.choice(at_bases)
                seq.append(base)
            fh.write(f'>{i}\n{"".join(seq)}\n')

    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()

