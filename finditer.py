"""Finditer in regex.

Works similar to findall
Returns: A callable iterator where elements are objects.
"""
import re

pattern = re.compile(r'(\w+) (\w+)')
result = pattern.finditer("Hello world i lived")
x = result.next()
print x.groups()
print x.span()
y = result.next()
print y.groups()
# another .next() will throw an error,
# indicating that there are no more elements
