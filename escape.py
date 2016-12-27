"""Escaping backlash characters.

A backlash is used to define metacharacters in regex.
So to cover them as characters, you need to escape them and use '\\'.
"""
import re

pattern = re.compile('\\\\')
another_pattern = re.compile(r'\\')
result = pattern.match("\\author")
print result.group()
res = another_pattern.match("\\at")
print res.group()
