'''
This file is a module that has steady-state equilibrium functions for
the capital and labor market clearing conditions and functions for the
interest rate and wage, the last two of which are functions of savings
b_2 in the two-period-lived overlapping generations model.
'''

# Put import commands below here


# Fill in the functions below


def get_K(b2):
    '''
    This will be a pretty simple function. Use steady-state equilibrium
    market clearing condition for the capital market (25) to return
    aggregate capital K as a function of savings b2.
    '''
    # Put code here.

    return K


def get_L(nvec):
    '''
    This function will also be a simple function. Use steady-state
    equilibrium market clearing condition for the labor market (24) to
    return aggregate labor L as a function of nvec, which is a numpy
    array (1-dimensional vector) with two elements n1 and n2
    '''
    # Put code here.

    return L


def get_r(b2, args):
    '''
    This function computes the steady-state interest rate as a function
    of savings b2 using steady-state equilibrium equation (28). The args
    input will have to be a tuple that includes nvec, alpha, A, and
    delta. Also, make sure to call your get_K() and get_L() functions
    inside of this function.
    '''
    # Put code here.

    return r


def get_w(b2, args):
    '''
    This function computes the steady-state wage as a function of
    savings b2 using steady-state equilibrium equation (29). The args
    input will have to be a tuple that includes nvec, alpha, and A.
    Also, make sure to call your get_K() and get_L() functions inside of
    this function.
    '''
    # Put code here.

    return w
