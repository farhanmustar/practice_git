# Single line comments start with a number symbol.

""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# You have numbers
3  # => 3

# Math is what you would expect
1 + 1   # => 2
8 - 1   # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# Enforce precedence with parentheses
1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8

# Boolean values are primitives (Note: the capitalization)
True   # => True
False  # => False

# negate with not
not True   # => False
not False  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True   # => True

# True and False are actually 1 and 0 but with different keywords
True + True # => 2
True * 8    # => 8
False - 5   # => -5

# Comparison operators look at the numerical value of True and False
0 == False  # => True
1 == True   # => True
2 == True   # => False
-5 != False # => True

# Using boolean logical operators on ints casts them to booleans for evaluation, but their non-cast value is returned
# Don't mix up with bool(ints) and bitwise and/or (&,|)
bool(0)     # => False
bool(4)     # => True
bool(-6)    # => True
0 and 2     # => 0
-5 or 0     # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True
