"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Adds two numbers

    Parameters
    ----------
        a : int, float
            One of the numbers to add
        b : int, float
            The other number to add

    Returns
    -------
        int, float
            The sum of a and b
    """
    return a+b

def simple_sub(a,b):
    """
    Subtracts one number from another

    Parameters
    ----------
        a : int, float
            The original number
        b : int, float
            The number to subtract from a

    Returns
    -------
        int, float
            a minus b
    """
    return a-b

def simple_mult(a,b):
    """
    Multiplies two numbers

    Parameters
    ----------
        a : int, float
            The first number in the multiplication
        b : int, float
            The other number in the multiplication

    Returns
    -------
        int, float
            a multiplied by b
    """
    return a*b

def simple_div(a,b):
    """
    Multiplies two numbers

    Parameters
    ----------
        a : int, float
            The first number in the multiplication
        b : int, float
            The other number in the multiplication

    Returns
    -------
        float
            a multiplied by b
    """
    return a/b

def poly_first(x, a0, a1):
    """
    Calculates the value of the first degree polynomial a0 + a1*x

    Parameters
    ----------
        x : int, float
            Value of x for which to evaluate the polynomial
        a0 : int, float
            Offset of the polynomial
        a1 : int, float
            Slope of the polynomial

    Returns
    -------
        float
            a0 + a1*x
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Calculates the value of the second degree polynomial a0 + a1*x + a2*x**2

    Parameters
    ----------
        x : int, float
            Value of x for which to evaluate the polynomial
        a0 : int, float
            Offset of the polynomial
        a1 : int, float
            Slope of the polynomial
        a1 : int, float
            Curvature of the polynomial

    Returns
    -------
        float
            a0 + a1*x + a2*x**2
    
    Examples
    --------
    >>> simple_math.poly_second(2,3,2,1)
    11
    >>> simple_math.poly_second(6,100,15,5)
    370
    """
    return poly_first(x, a0, a1) + a2*(x**2)