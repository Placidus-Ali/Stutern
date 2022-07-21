from subprocess import getstatusoutput, getoutput
#!/usr/bin/env python3
"""test for hello.py"""

import os


file_name = '.\hello.py'


#-------------------------------------------------
def test_exist():
    """exist"""

    assert os.path.isfile(file_name)

#--------------------------------------------------
def test_runnable():
   """Run using python3"""

   out = getoutput(f'python3 {file_name}')
   assert out.strip()  == "Hello World!"


#----------------------------------------------------
# def test_executable():
#         """Says 'Hello, World' by default"""

#     out = getoutput(prg)
#     assert out.strip() == "Hello, World!"

def test_executable():
    """check if the file_name will execute"""

    out = getoutput(file_name)
    assert out.lstrip() == "Hello World!" 

#------------------------------------------------------
def test_usage():
    """"usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f' {file_name} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

#--------------------------------------------------------
def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f' {file_name} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'