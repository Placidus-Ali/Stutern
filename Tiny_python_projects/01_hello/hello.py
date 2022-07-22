#!/usr/bin/env python3
#say hello

import argparse
from email import parser

parser = argparse.ArgumentParser(description= 'say hello')
parser.add_argument('-n', '--name', metavar='Name', default='World', help='Name to greet')
args = parser.parse_args()
name = args.name

print('Hello ' + name + '!')
