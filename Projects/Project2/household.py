'''
This file is a module that has steady-state equilibrium functions for
the household consumptions c1 and c2 as well as the marginal utility of
consumption in the two-period-lived overlapping generations model.
'''

# Put import commands below here


# Fill in the functions below


def get_c1(b2, args):
    '''
    Use steady-state equilibrium young age s=1 budget constraint (26) to
    return individual consumption c1 as a function of b2 and arguments.
    Make sure to use FirmsMC.get_w() function inside of this function.
    So the args intput will be a tuple that has all the arguments
    necessary in equation (26) as well as whatever arguments are
    necessary in FirmsMC.get_w().
    '''
    # Put code here.

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
    # Put code here.

    return c2


def get_MUc(c, gamma):
    '''
    This function is a very simple function. It takes as arguments a
    consumption level c and a coefficient of relative risk aversion
    gamma and computes the marginal utility of that consumption using
    the expression in equation (9).
    '''
    # Put code here.

    return MUc
