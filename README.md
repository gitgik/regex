# regex
All things regular expression: implemented in python.

#### Purpose
Regular expressions are simple yet many programmers fear them. You just have to understand them and what they do to see their vast benefits in computing.
As you learn them, you will get to see how powerful they are in string manipulation, grouping, look aheads and searching in general. :-)

#### Usage
We learn by doing. Simply run the files in your prompt to see the results and experiment on different inputs.
But before this, first things first:

1. Clone the flan to your local as such:

```
    $ git clone https://github.com/gitgik/regex.git
```

2. Run it on your local command line

```
   $ python <filename>.py
```

#### Tags to use
| Element        | Description                                              |
|:--------------:|:--------------------------------------------------------:|
| .              | This element matches any character except \n             |
| \d             | This matches any digit [0-9]                             |
| \D             | This matches non-digit characters [^0-9]                 |
| \s             | This matches whitespace character [ \t\n\r\f\v]          |
| \S             | This matches non-whitespace character [^ \t\n\r\f\v]     |
| \w             | This matches alphanumeric character [a-zA-Z0-9_]         |
| \W             | This matches any non-alphanumeric character [^a-zA-Z0-9] |

#### Quantifiers to use
| Quantifier        | Description       |   Example  | Sample match          |
|:-----------------:|:-----------------:|:----------:|:---------------------:|
| +                 | one or more       | \w+        | ABCDEF097             |
| {2}               | exactly 2 times   |  \d{2}     |   01                  |
| {1,}              | one or more times |  \w{1,}    | smiling               |
| {2,4}             | 2 to 4 times      |  \w{2,4}   | 1234                  |
| *                 | 0 or more times   |  A*B       | AAAAB                 |
| ?                 | once or none(lazy)|  \d+?      | 1 in 12345            |

### Boundaries
Most regular expressions usually start with a `^` and end with a `$`
But when used in square brackets [^...] means `not`.
e.g `[^\s] will match anything that is not a whitespace character `



#### Benchmarking
Benchmark.py measures the time taken for a regex to execute. Also, test your regex with different inputs because with small ones, regex is fast enough.

To benchmark, go to your python prompt and run this:
```
    >>> from benchmark import test
    >>> # define your regex in a function here
    >>> test(<function-name>, "<text/string-input>")
```

####PS

Ensure you read the docstrings and comments to understand how the code works.


