#!/user/bin/env python3
# Say Hello World

import argparse

parser = argparse.ArgumentParser(description= 'say Hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()
name = args.name

print("Hello, "+ name + "!")

