#!/usr/bin/env python3
"""
Author : Julia
Date   : 2025-02-05
Purpose: say howdy
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="say howdy", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-n",
        "--name",
        help="A name to greet",
        metavar="str",
        type=str,
        default="Stranger",
    )

    parser.add_argument(
        "-g", "--greeting", help="A greeting", metavar="str", type=str, default="Howdy"
    )

    parser.add_argument("-e", "--excited", help="A boolean flag", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    name = args.name
    greeting = args.greeting
    excited = args.excited

    if excited:
        print(f"{greeting}, {name}!")
    else:
        print(f"{greeting}, {name}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
