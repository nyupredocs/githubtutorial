'''
This file is a module that has steady-state equilibrium functions for
solving the household steady-state equilibrium Euler equation for
savings in the two-period-lived overlapping generations model.
'''

# Put import commands below here


# Fill in the functions below


def eul_err(b2, *args):
    '''
    This function computes the Euler error (simple difference) implied
    by the steady-state equilibrium Euler equation (30). This function
    will need to call the FirmsMC.get_r(), FirmsMC.get_w() functions as
    household.get_c1(), household.get_c1(), and household.get_MUc()
    functions. You will need to make sure that the arguments passed into
    this function are sufficient for everything you need to calculate
    the error form of (30).
    '''
    # Put code here.

    return error


def get_b2(args):
    '''
    This function will solve for the optimal individual savings by
    solving for the b2 that solves the steady-state equilibrium Euler
    equation (30). Use the scipy.optimize.root() function to solve for
    the root of the Euler equation (30), the euler error. This means
    that the target of your root finder will be the eul_err() function
    above
    '''
    # Put code here.

    return b2
