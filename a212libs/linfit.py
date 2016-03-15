def LineFitWt(x, y, dy):
    """
    Calculates the linear agression with weighting uncertainties
    (chi-squared,fitting)

    Parameters
    ----------

    x: array (any shape) or scalar (float32, float64  or complex)

    y: array (any shape) or scalar (float32, float64  or complex) must be same
        length as x

    dy: uncertainty of each indivdual datapoint must also be same length as x
        and y

    Returns
    -------

    slope of best fitting line,
    y intercept of best fitting line,
    uncertainty of best fitting line,
    uncertainty of y intercept,

    In the above order.

    Example
    -------
    >>>LineFitWt(2.,3.,1)
    ***FINISH THIS!!!!****


    """
    x = np.atleast_1d(x)
    the_shape = x.shape
    if x.dtype not in [np.float32, np.float64, np.complex]:
        raise ValueError(
            "expected dtype of float32,float64 or complex, got {}",
            format(x.dtype))

    y = np.atleast_1d(y)
    the_shape = y.shape
    if y.dtype not in [np.float32, np.float64, np.complex]:
        raise ValueError(
            "expected dtype of float32,float64 or complex, got {}",
            format(y.dtype))

    dy = np.atleast_1d(dy)
    the_shape = x.shape
    if dy.dtype not in [np.float32, np.float64, np.complex]:
        raise ValueError(
            "expected dtype of float32,float64 or complex, got {}",
            format(dy.dtype))

    #make sure all arrays are the saem length
    if len(x) != len(y) or len(x) != len(dy):
        raise ValueError("input values not of equil length")

    else import numpy as np
    import doctest
    import numpy.testing as ntest

    dy2 = dy**2.
    denom= np.sum(1/(dy**2.))  # Pine 7.14
    xnumerator = np.sum(x/dy2)
    ynumerator = np.sum(y/dy2)
    xhat = xnumerator/denom
    yhat = ynumerator/denom
    bnum = np.sum((x - xhat)*y/dy2)
    bdenom = np.sum((x - xhat)*x/dy2)

    slope = bnum/bdenom
    yint = yhat - slope*xhat

    sigma_bdenom = (np.sum((x-xhat)*(x/dy**2)))
    sigma_b = np.sqrt(1/sigma_bdenom)

    sigma_anumerator = np.sum((x**2)/(dy**2))
    sigma_adenom = np.sum(1/dy**2)
    sigma_a = sigma_b*sigma_anumerator/sigma_adenom

    return slope,yint,sigma_a,sigma_b
