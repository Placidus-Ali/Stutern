from subprocess import getstatusoutput, getoutput
#!/usr/bin/env python3
"""test for hello.py"""

import os


prg = '.\hello.py'


#-------------------------------------------------
def test_exist():
    """exist"""

    assert os.path.isfile(prg)

#--------------------------------------------------
def test_runnable():
   """Run using python3"""

   out = getoutput(f'python3 {prg}')
   assert out.strip()  == "Hello World!"


#----------------------------------------------------

def test_executable():
    """Sy 'Hello Wolrd!' by defualt"""
    
    out = getoutput(prg)
    assert out.strip() == '' 

#------------------------------------------------------
def test_usage():
    """"usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f' {prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('World')

#--------------------------------------------------------
def test_input():
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f' {prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'