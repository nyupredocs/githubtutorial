'''
This file is a script that solves for the steady-state in the two-
period-lived overlapping generations model given some parameter values.
'''

# Put import commands below here
import numpy as np

# Set parameter values

# Household parameters
n1 = ?
n2 = ?
nvec = np.array([n1, n2])
gamma = ?
beta = ?

# Firm parameters
A = ?
alpha = ?
delta = ?


# Solve for b2 given parameters




# Solve for all the other endogenous variables given parameter values
# and optimal b2

# Solve for all the other endogenous variables given parameter values
# and optimal b2
c1 = w*n1 - b2
c2 = (1 + r)*b2 + w*n2
C = c1 + c2

r = alpha*A*(L/K)**(1 - alpha) - delta
w = ((1 - alpha)*A*(K/L))**alpha

K = b2
L = np.sum(nvec)
I = K - (1 - delta)*K
Y = C + I

# Print steady-state equilibrium endogenous variables
