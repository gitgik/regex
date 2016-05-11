"""String manipulation.

2. re.sub(replacement, string)
This operation return the resulting string after
replacing the matched pattern with the replacement.

3. re.subn(replacement, string, count=0)
Same operation as sub.
Returns a tuple with the new string and the number of substitutions made.
"""

import re

pattern = re.compile(r"[0-9]+")
result = pattern.sub("-", "there is only 1 thing 2 do")
print result

# this example replaces matched 00 with - to
# resulting in 1--0
print re.sub('00', '-', '100000')


# subn
text = "imagine a *world*, a new *world*"
p = re.compile(r"\*(.*?)\*")
res = p.subn(r"<b>\g<1><\\b>", text)
print res
