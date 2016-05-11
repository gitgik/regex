"""Group operation gives the subgroups of the match.

1. re.group()
Returns the entire match if no args are passed.

2. re.groups([default])
Returns the tuple with all the sub groups.
"""
import re

pattern = re.compile(r"(\w+) (\w+)")
match = pattern.search("Hello world")
print match.group(0)  # prints Hello world
print match.group(1)  # prints Hello
print match.group(2)  # prints world
# print match.group(3)  # Index Error: no such group thrown
print match.group(0, 2)  # prints world


# groups
print match.groups()
