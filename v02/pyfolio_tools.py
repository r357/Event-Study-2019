# -*- coding: utf-8 -*-
import numpy as np
import scipy.stats as scs


# Calculates Log Returns
def LogReturns(data):
    """ Given data (Pandas DataFrame) will be transformed into log-returns.
    """   
    log_returns = np.log(data / data.shift(1))
    return(log_returns)


# PrintStatistics tools
def print_statistics(data):          
    """ Prints statistics
    (size, min, max, mean, std, skew, kurtosis)
    data: ndarray object to generate statistics on
    """
    
    sta = scs.describe(data)
    print()
    print("%14s %15s" % ('statistic', 'value'))
    print(30 * "-")
    print("%14s %15.5f" % ('size', sta[0]))
    print("%14s %15.5f" % ('min', sta[1][0]))
    print("%14s %15.5f" % ('max', sta[1][1]))
    print("%14s %15.5f" % ('mean', sta[2]))
    print("%14s %15.5f" % ('std',  np.sqrt(sta[3])))
    print("%14s %15.5f" % ('skew',  sta[3]))
    print("%14s %15.5f" % ('kurtosis',  sta[4]))
    print()


# NormalityTest tools
def normality_test(data):
    """ Tests for normality distribution of given data set
    (skew, skew-p, kurtosis, kurtosis-p, normality-p)
    data: ndarray object to generate statistics on 
    """ 
    
    print()
    print("Skew of data set %14.3f" % scs.skew(data))
    print("Skew test p-value %14.3f" % scs.skewtest(data)[1])
    print("Kurtosis of data set %14.3f" % scs.kurtosis(data))
    print("Kurtosis test p-value %14.3f" % scs.kurtosistest(data)[1])
    print("Normality test p-value %14.3f" % scs.normaltest(data)[1])
    print()


# STATISTICS
def statistics(data, noa, port_weights=1, year=252):
    """
    data (array-like): weights for securities in portfolio. 
    port_weights=1: equal weights are assigned
    noa = number of assets
    pret (float): E(returns)
    pvol (float): E(volatility)
    pret/pvol (float): Sharpe Ratio for rf=0
    """
      
    if port_weights == 1:
            port_weights = np.random.random(noa)
            port_weights /= np.sum(port_weights)
    log_returns = LogReturns(data)
    weights = np.array(port_weights)
    pret = np.sum(log_returns.mean() * port_weights) * year
    pvol = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * year, port_weights)))
    return np.array([pret, pvol, pret / pvol])





# VARIANCE / VOLATILITY
def min_func_variance(weights):
    return statistics(weights)[1] ** 2

def min_func_port(weights):
    return statistics(weights)[1]

# MARKOWITZ - Related
def min_func_sharpe(weights):
    return -statistics(weights)[2]

