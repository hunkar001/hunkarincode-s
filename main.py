import math

def kokvarmi(sayi):
    """
    >>> kokvarmi(16)
    True
    >>> kokvarmi(17)
    False
    >>> kokvarmi(36)
    True

    """
    return math.sqrt(sayi)%1 == 0

if __name__ == "__main__" :

    import doctest
    doctest.testmod(verbose=True)

    