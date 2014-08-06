from math import sqrt
from copy import deepcopy

def linreg(X, Y):
    """
    Summary
        Linear regression of y = ax + b
    Usage
        real, real, real = linreg(list, list)
    Returns coefficients to the regression line "y=ax+b" from x[] and y[], and R^2 Value
    """
    if len(X) != len(Y):
        raise ValueError('unequal length')

	# Handles the horizontal 2-point line case
    if len(Y) == 2 and Y[0] == Y[1] :
        return 0, Y[0], 1
    #/////////////////////////////////////////

    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    a, b = (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det
    meanerror = residual = 0.0
    for x, y in zip(X, Y):
        meanerror = meanerror + (y - Sy/N)**2
        residual = residual + (y - a * x - b)**2
    RR = 1 - residual/meanerror
    return a, b, RR


def partialreg(X, Y, threshold, backwards = "no", cutoff_size_input = 10, cutoff_size_in_percent = "yes") :
    """
    Summary
        Linear regression of y = ax + b
        Cuts away parts of X and Y if RR is inferior to  the threshold
    Usage
        [real, real, real], int, int = partialreg(list, list, real, optional str, opttional int, optional string)
    Return coefficients to the regression line "y=ax+b" from x[] and y[], R^2 value,
    the length of X and Y treated by the function, and the cutoff size.

    If the backwards flag is set to "backwards", the cutoff is operated at the beginning of the lists ("backwards")
    cutoff_size determines the portion of the list that is cut off is the regression fails to meet the threshold
    The cutoff_size_in_percent flag determines if cutoff_size is to be treated as an integer or a percentage ("no")
    """

    # Flags manipulation
    bk = 0
    cpct = 1
    cutoff_size = cutoff_size_input
    if backwards == "backwards" :
        bk = 1
    if cutoff_size_in_percent == "no" :
        cpct = 0
    #///////////////////

    new_X = deepcopy(X)
    new_Y = deepcopy(Y)
    cutoff_return = 0

    reg_results = linreg(new_X,new_Y)
    # While R squared < threshold, keep cutting the lists
    while reg_results[2] < threshold :
        # If the cuttof becomes too small / large, set it back to 1 (integer)
        if (len(new_X) - int(cutoff_size * (1 + cpct * (len(new_X)/100 - 1)))) < 3 or int(cutoff_size * (1 + cpct * (len(new_X)/100 - 1))) < 1:
            cpct = 0
            cutoff_size = 1
        # Cutoff data
        del new_X[(bk - 1) * int(cutoff_size * (1 + cpct * (len(new_X)/100 - 1))):(1 - bk) * len(new_X) + bk * int(cutoff_size * (1 + cpct * (len(new_X)/100 - 1)))]
        del new_Y[(bk - 1) * int(cutoff_size * (1 + cpct * (len(new_Y)/100 - 1))):(1 - bk) * len(new_Y) + bk * int(cutoff_size * (1 + cpct * (len(new_Y)/100 - 1)))]
        cutoff_return += 1
        reg_results = linreg(new_X, new_Y)

    return reg_results, len(new_X), cutoff_return
	