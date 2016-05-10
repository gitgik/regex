"""String manipulation.

2. re.sub(replacer, string)
This operation return the resulting string after
replacing the matched pattern with the replacement.
"""
import re

pattern = re.compile(r"[0-9]+")
result = pattern.sub("-", "there is only 1 thing 2 do")
print result

# another example
print re.sub('00', '-', '100000')
