#!/usr/bin/env python3

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="choose the article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', 
                        metavar='word', 
                        help='The thing that we see')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.word)
    
    # word = args.word
    # article = 'an' if word[0].lower() in 'aeiou' else 'a'

    # print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()