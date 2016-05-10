"""String searching in python.

Matches the pattern at any location within the str
"""
import re
pattern = re.compile(r"^<html>", re.MULTILINE)
result = pattern.search("<html>")
# search succeeds thanks to multiline
another = pattern.search("  \n<html>")
print result.group(), another.group()

# The pos works if it's less  of equal to the string
res = pattern.search("<div><div>\n<html>", 4)
bad = pattern.search("  \n<html>", 4)  # Wont work
print res.group(), bad
