"""String matching in python.

e.g x.match('pattern')

First, a re.match matches the
pattern only at the beginning of the string.
"""
import re

# recompile regular expression.
patt = re.compile(r'<HTML>')
patt.match("HTML")
# or you could just as well do this
print re.match(r'<html>', "<html>")
# this returns None if string does not start with 'html'
another_one = re.match(r'html', 'SOMETHINGhtmlcowpig')
print another_one

# optional pos parameter specifies where to start searching
pattern = re.compile(r'html')
pattern.match('__html', 2)
print pattern
