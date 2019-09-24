'''
This file is a module that has steady-state equilibrium functions for
solving the household steady-state equilibrium Euler equation for
savings in the two-period-lived overlapping generations model.
'''

# Put import commands below here
import FirmsMC as fmc
import household as hh

import scipy.optimize as opt
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
    gamma = args[5]

    # Calculate LHS of equation #30
    c1 = hh.get_c1(b2, args)

    MU_c1 = hh.get_MUc(c1, gamma)

    # Calculate RHS of equation #30
    beta = args[4]

    r = fmc.get_r(b2, args)

    c2 = hh.get_c2(b2, args)

    MU_c2 = hh.get_MUc(c2, gamma)

    # Calculate error
    error = MU_c1 - beta * (1 + r) * MU_c2

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
    b_init = 0.01
    b_result = opt.root(eul_err, b_init, args=args)

    b2 = b_result.x[0]
    b2_success = b_result.success
    b2_error = b_result.fun[0]
    print('Euler error success=' + str(b2_success) + '. Euler error =' +
          str(b2_error))

    return b2, b2_success, b2_error
