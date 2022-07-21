#!/usr/bin/env python3

import argparse
from email import parser
import os
import sys

#--------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description= 'Say Hello'
        formatter_class= argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--n', 
                        '--name',
                        help='Name to greet',
                        metavar='name',
                        type=str
                        default='World')
    
    return parser.parse_args()

def main():
    """Make a jazz noise here"""

    args = get_args()
    print('Hello, + args.name' + '!')

if __name__ == '__main__' :
    main()
    
