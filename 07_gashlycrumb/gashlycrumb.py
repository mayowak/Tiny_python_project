#!/usr/bin/env python3
"""
Author : Mayowa Kolawole
Date   : 2020-12-20
Purpose: Gashlycrumb
"""

import argparse
import os
import sys
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters',
                        metavar='letter',
                        nargs='+',
                        help='letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Get main"""
    
    args = get_args()

    lookup = {}
    for line in args.file:
        char = line[0].upper()
        lookup[char] = line.rstrip()

    #pprint(lookup)

    for letter in args.letters:
        if letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print(f'I do not know "{letter}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()