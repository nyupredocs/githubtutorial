'''
This file is a module that has steady-state equilibrium functions for
solving the household steady-state equilibrium Euler equation for
savings in the two-period-lived overlapping generations model.
'''

# Put import commands below here
import FirmsMC
import household

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


    #Calculate LHS of equation #30
    c1 = household.get_c1(b2, args)

    MUc1 = household.get_MUc(c1, gamma)

    LHS = hh.get_MUc(c1, gamma)



    #Calculate RHS of equation #30
    beta = args[4]

    r = FirmsMC.get_r(b2, args)

    c2 = household.get_c2(b2, args)

    MUc2 = household.get_MUc(c2, gamma)

    RHS =  beta * (1 + r) * MUc2


    #Calculate using LHS and RHS
    error = LHS - RHS



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
    b_init = 2.0
    b_result = opt.root(eul_err, b_init, args=args)

    b2 = b_result.x[0]

    return b2
