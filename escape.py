"""Escaping backlash characters.

A backlash is used to define metacharacters in regex.
So to cover them as characters, you need to escape them and use '\\'.
"""
import re

pattern = re.compile('\\\\')
another_pattern = re.compile(r'\\')
print pattern.match("\\author")
print another_pattern.match("\\at")
