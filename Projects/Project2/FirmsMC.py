'''
This file is a module that has steady-state equilibrium functions for
the capital and labor market clearing conditions and functions for the
interest rate and wage, the last two of which are functions of savings
b_2 in the two-period-lived overlapping generations model.
'''

# Put import commands below here
import numpy as np


def get_K(b2):
    '''
    This will be a pretty simple function. Use steady-state equilibrium
    market clearing condition for the capital market (25) to return
    aggregate capital K as a function of savings b2.
    
    Parameters
    ----------
    b2 : numeric
        value for b_2

    Returns
    -------
    K : numeric
        returns value for K
    '''
    K = b2

    return K

def get_L(nvec):
    '''
    This function will also be a simple function. Use steady-state
    equilibrium market clearing condition for the labor market (24) to
    return aggregate labor L as a function of nvec.
    
    Parameters
    ----------
    nvec : np.array
        1 dimensional vector with n1 and n2

    Returns
    -------
    L : numeric
        returns value for L
    '''
    L= np.sum(nvec)

    return L

def get_r(b2, args):
    '''
    This function computes the steady-state interest rate as a function
    of savings b2 using steady-state equilibrium equation (28). 
    
    Parameters
    ----------
    b2 : numeric
        Value for b_2 variable
    args : tuple
        Tuple ordered as:
            - nvec: np.array (1 dimension) with n1 and n2
            - alpha: numeric [0,1]
            - A: numeric
            - delta: numeric
    Returns
    -------
    r : numeric
        returns value for r
    '''
    
    nvec, alpha, A, delta = args
    K = get_K(b2)
    L = get_L(nvec)
    r = alpha * A * (L / K) ** (1 - alpha)  - delta

    return r

def get_w(b2, args):
    '''
    This function computes the steady-state wage as a function of
    savings b2 using steady-state equilibrium equation (29).
    
    Parameters
    ----------
    b2 : numeric
        Value for b_2 variable
    args : tuple
        Tuple ordered as:
            - nvec: np.array (1 dimension) with n1 and n2
            - alpha: numeric [0,1]
            - A: numeric
    Returns
    -------
    w : numeric
        returns value for w
    '''
    
    nvec, alpha, A = args
    K = get_K(b2)
    L = get_L(nvec)
    w = (1 - alpha) * A * (K / L) ** alpha

    return w
