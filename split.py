"""String manipulation.

1. re.split(string, maxsplit=0),
This string split is based on the matches of the given pattern.
Returns a list of elements that match the splitting pattern.

2. re.sub,
"""
import re

# first lets split a string into words
pattern = re.compile(r"\W")  # Match non alphanumeric xters.
result = pattern.split("hello world")
print result  # will split using the whitespace match.

# specifying the maxsplit parameter
# split a max of 2 times then return the rest of the string too.
print pattern.split("I have a dream in code", 2)

# To capture the pattern too, we use groups
p = re.compile(r"(-)")
print p.split("hello-world")  # - character is also split :-)
