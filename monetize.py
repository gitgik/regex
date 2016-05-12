"""Create a comma seperated number from a non-formatted number."""
import re
number = input("Enter your number\n")


def monetizer(number):
    """A function that adds a thousands separator using comma characters."""
    number = str(number)
    test_int = int(number)
    if type(test_int) == int:
        # Format into groups of three from the right to the left
        pattern = re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))')
        return pattern.sub(r'\g<0>,', number)
    return False
# Function call
print monetizer(number)
