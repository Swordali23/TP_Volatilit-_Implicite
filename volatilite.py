import matplotlib.pyplot as plt
import numpy as np
from numpy import nbytes, zeros,array,dot,linspace, linalg
from math import sqrt, pi, exp, erfc

## volatility for a call option ##

def volatilite(S, E, T, r, CO, sigma):

    d1 = (np.log(S/E) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    Ee = E*np.exp(-r*T)

    N1 = 1/2*erfc(-d1/np.sqrt(2))
    N2 = 1/2*erfc(-d2/np.sqrt(2))
    c = S*N1 - Ee*N2
    F = CO - c

    return F

def execute(a, b):
    T = 3 # maturity
    r = 0.05 # risk free rate
    CO = 100 # call option price
    S = 300 # stock price
    E = 100 # strike price

    a1 = a
    b1 = b
    d = (a+b)/2
    i = 0

    while i<300:
        if volatilite(S, E, T, r, CO, a)*volatilite(S, E, T, r, CO, d) < 0:
            b = d
        else:
            a = d
        d = (a+b)/2
        i = i+1
    
    plt.plot([a1, b1], [volatilite(S, E, T, r, CO, a1), volatilite(S, E, T, r, CO, b1)], 'r')
    plt.show()

    return d


a = 5.0
b = 10.0
d = execute(a, b)
print('Volatility is: ', d)


## volatility for a put option ##

def volatilite(S, E, T, r, PO, sigma):
    
        d1 = (np.log(S/E) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
    
        Ee = E*np.exp(-r*T)
    
        N1 = 1/2*erfc(-d1/np.sqrt(2))
        N2 = 1/2*erfc(-d2/np.sqrt(2))
        p = Ee*N2 - S*N1
        F = PO - p
    
        return F

def execute(a, b):
    T = 3 # maturity
    r = 0.05 # risk free rate
    PO = 100 # put option price
    S = 300 # stock price
    E = 100 # strike price
    
    a1 = a
    b1 = b
    d = (a+b)/2
    i = 0
    
    while i<300:
        if volatilite(S, E, T, r, PO, a)*volatilite(S, E, T, r, PO, d) < 0:
            b = d
        else:
            a = d
        d = (a+b)/2
        i = i+1
    
    plt.plot([a1, b1], [volatilite(S, E, T, r, PO, a1), volatilite(S, E, T, r, PO, b1)], 'r')
    plt.show()
    
    return d

a = 5.0
b = 10.0
d = execute(a, b)
print('Volatility is: ', d)






