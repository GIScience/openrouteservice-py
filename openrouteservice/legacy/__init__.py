__version__ = "2.3.3"

def get_ordinal(number):
    """Produces an ordinal (1st, 2nd, 3rd, 4th) from a number."""

    if number == 1:
        return "st"
    elif number == 2:
        return "nd"
    elif number == 3:
        return "rd"
    else:
        return "th"