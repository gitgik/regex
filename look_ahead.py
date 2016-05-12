"""Look ahead mechanism in regular expressions.

use (?=)
"""
import re

pattern = re.compile(r'(?=fox)')
result = pattern.search("The quick brown fox")
print result

"""
Match any word followed by a comma.
The example below is not the same as re.compile(r"\w+,")
For this will result in ['me,', 'myself,']
"""
patt = re.compile(r"\w+(?=,)")
res = patt.findall("Me, myself, and I")
print res

"""Use alternation (|) to match
any word followed by comma or a dot.
"""
p = re.compile(r'\w+(?=,|\.)')
results = p.findall("Here they are: Tom, Dick, and Harry.")
print results
