'''
This file is a module that has steady-state equilibrium functions for
the household consumptions c1 and c2 as well as the marginal utility of
consumption in the two-period-lived overlapping generations model.
'''

import FirmsMC


def get_c1(b2, args):
    '''
    Use steady-state equilibrium young age s=1 budget constraint (26) to
    return individual consumption c1 as a function of b2 and arguments.
    Make sure to use FirmsMC.get_w() function inside of this function.
    So the args intput will be a tuple that has all the arguments
    necessary in equation (26) as well as whatever arguments are
    necessary in FirmsMC.get_w().
    '''
    # unpack arguments
    nvec, alpha, A, delta, beta, gamma = args

    # get w, n
    w = FirmsMC.get_w(b2, args=args)
    n1 = nvec[0]

    # specify c1
    c1 = w * n1 - b2

    return c1


def get_c2(b2, args):
    '''
    Use steady-state equilibrium old age s=2 budget constraint (27) to
    return individual consumption c2 as a function of b2 and arguments.
    Make sure to use FirmsMC.get_r() and FirmsMC.get_w() functions
    inside of this function. So the args intput will be a tuple that has
    all the arguments necessary in equation (27) as well as whatever
    arguments are necessary in FirmsMC.get_r() and FirmsMC.get_w().
    '''
    # unpack arguments
    nvec, alpha, A, delta, beta, gamma = args

    r = FirmsMC.get_r(b2, args)
    w = FirmsMC.get_w(b2, args)
    n2 = nvec[1]

    # specify c2
    c2 = (1 + r) * b2 + w * n2

    return c2


def get_MUc(c, gamma):
    '''
    This function is a very simple function. It takes as arguments a
    consumption level c and a coefficient of relative risk aversion
    gamma and computes the marginal utility of that consumption using
    the expression in equation (9).
    '''
    # error if inputs take disallowed values
    if c <= 0:
        raise Exception
    if gamma <= 0:
        raise Exception

    # specify marginal utility
    MUc = c ** (-gamma)

    return MUc
