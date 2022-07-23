#!/usr/bin/env python3

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('Iteam',
                        metavar='str',
                        nargs='+',
                        help='Iteams we are bringing')

    parser.add_argument('-s',
                        '--sorted',
                        help='whether to sort the iteams',
                        action='store_true')

    
    return parser.parse_args()


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    print(args.items)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()