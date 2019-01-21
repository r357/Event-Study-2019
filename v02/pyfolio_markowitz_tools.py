import numpy as np
import pandas as pd
import pyfolio_tools as pft
import scipy.optimize as sco


# LOG RETURNS
def log_r(data):
    log_returns = np.log(data / data.shift(1))
    return log_returns


# NEW STATS FOR MARKOWITZ
def statistics(weights, data):
    '''
    weights (array-like): weights for securities in portfolio
    pret (float): E(returns)
    pvol (float): E(volatility)
    pret/pvol (float): Sharpe Ratio for rf=0
    '''
    weights = np.array(weights)
    rets = log_r(data)
    pret = np.sum(rets.mean() * weights) * 252
    pvol = np.sqrt(np.dot(weights.T, np.dot(rets.cov() * 252, weights)))
    return np.array([pret, pvol, pret / pvol])


# VARIANCE / VOLATILITY
def min_func_variance(weights, data):
    return statistics(weights, data)[1] ** 2

def min_func_port(weights, data):
    return statistics(weights, data)[1]


# MARKOWITZ - Related
def min_func_sharpe(weights, data):
    return -statistics(weights, data)[2]


# SR
def max_sr_port(data, noa):    
    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x)-1})
    bnds = tuple((0, 1) for x in range(noa))   
    opts = sco.minimize(min_func_sharpe, 
                        noa * [1. / noa,],
                        data,
                        method = 'SLSQP', 
                        bounds=bnds, 
                        constraints=cons)
    return opts['x']


# MIN VAR
def min_var_port(data, noa):
    cons = ({'type': 'eq', 'fun': lambda x: np.sum(x)-1})
    bnds = tuple((0, 1) for x in range(noa))  
    optv = sco.minimize(min_func_variance, 
                        noa * [1. / noa,],
                        data,
                        method='SLSQP',
                        bounds=bnds, 
                        constraints=cons)
    return optv['x']
    

# SHORT PORTFOLIO
def short_port(data, noa):
    
    rets = log_r(data)
    # Mean return for each stock (in array)
    r = np.array(np.mean(rets, axis=0))  
    # Covariance matrix between stocks (in array)
    S = np.array(rets.cov())  
    # Inverse of the covariance matrix
    Si = np.linalg.inv(S)    
    # Vector of 1's equal in length to r
    e = np.ones(len(r))
    
    # a, b, c coefficients
    a = np.matmul(np.matmul(r,Si),r)
    b = np.matmul(np.matmul(r,Si),e)
    c = np.matmul(np.matmul(e,Si),e) # same as Si.sum()
    
    # Lambda1 and Lambda2 coefficients
    l1 = (c*mu - b) / (a*c - b*b)
    l2 = (-b*mu + a) / (a*c - b*b)
    
    # Calculate weights
    weights = l1*(np.matmul(Si,r)) + l2*(np.matmul(Si,e))
    print("Short weights checksum:", w.sum())
    return weights
