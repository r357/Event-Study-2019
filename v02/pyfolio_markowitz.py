# -*- coding: utf-8 -*-
import numpy as np
import pyfolio_tools as pft
import scipy.optimize as sco
import matplotlib.pyplot as plt
import pyfolio_markowitz_tools as pmt


# MAX SHARPE RATIO PORTFOLIO
def Max_SR_Portfolio(data, noa):

    max_sr_weights = pmt.max_sr_port(data, noa)    
    max_sr_rets = pmt.statistics(max_sr_weights, data)
    
    print(50*"_")
    print("MAX SHARPE RATIO PORTFOLIO")
    print("E(r), E(var), E(SR)")
    print(max_sr_rets.round(3))
    print("Weights:")
    print(max_sr_weights.round(3))
    return(max_sr_rets, max_sr_weights)


# MIN VARIANCE PORTFOLIO
def Min_Var_Portfolio(data, noa):
    
    min_var_weights = pmt.min_var_port(data, noa)
    min_var_rets = pmt.statistics(min_var_weights, data)
    
    print(50*"_")
    print("MIN VARIANCE PORTFOLIO")
    print("E(r), E(var), E(SR)")
    print(min_var_rets.round(3))
    print("Weights:")
    print(min_var_weights.round(3))    
    return(min_var_rets, min_var_weights)
    
    
def Current_Portfolio(current_portfolio, data):
    
    curr_port_rets = pmt.statistics(current_portfolio, data)
    
    print(50*"_")
    print("CURRENT PORTFOLIO")
    print("E(r), E(var), E(SR)")
    print(curr_port_rets.round(3))
    print("Weights:")
    print(current_portfolio.round(3))   
    return(curr_port_rets, current_portfolio)


def Short_Portfolio(data, noa):
    
    short_weights = pmt.short_port(data, noa)
    short_rets = pmt.statistics(short_weights, data)

    print(50*"-")
    print("SHORT PORTFOLIO")
    print("E(r), E(var), E(SR)")
    print(short_rets.round(3))
    print("Weights:")
    print(short_weights.round(3))
    return(short_rets, short_weights)
    


# MARKOWITZ
def Wrapper_Markowitz_gData(data, noa=1, pie=1, 
                            simulations=2000, current_portfolio=0, short=True):    
    
    """ To be used only if data is downloaded via Wrapper_GetData
    """    
    
    # Get number of assets
    if noa==1:
        noa = data[3]    
    # Assign Random weights
    weights = np.random.random(noa)
    weights /= np.sum(weights)    
    # Log returns    
    rets = pmt.log_r(data)    
    # Get symbols
    symbols = data.columns.tolist()
    
    
    """ RANDOM PORTFOLIO COMPOSITION """
    """
    _rets: returns
    _vols: volatility
    """ 
    prets = []
    pvols = []           
    for p in range(simulations):
        weights = np.random.random(noa)
        weights /= np.sum(weights)
        prets.append(np.sum(rets.mean() * weights)*252)
        pvols.append(np.sqrt(np.dot(weights.T, np.dot(rets.cov()*252, weights))))

    prets = np.array(prets)
    pvols = np.array(pvols)


    """ MAXIMUM SHARPE RATIO """
    max_sr = Max_SR_Portfolio(data, noa)
    max_sr_parm = max_sr[0]
    max_sr_weights = max_sr[1]
    if pie == 1:
        plt.figure(figsize=plt.figaspect(1))
        plt.pie(max_sr_weights, labels=symbols, autopct='%.2f')
        plt.figure()

    
    """ MINIMUM VARIANCE """
    min_var = Min_Var_Portfolio(data, noa)
    min_var_parm = min_var[0]
    min_var_weights = min_var[1]
    if pie == 1:
        plt.figure(figsize=plt.figaspect(1))
        plt.pie(min_var_weights, labels=symbols, autopct='%.2f')
        plt.figure()
    
    
    """ CURRENT PORTFOLIO """
    if current_portfolio is not 0:
        curr_port = Current_Portfolio(current_portfolio, data)
        curr_port_parm = curr_port[0]
    
    
    """ SHORT-ENABLED PORTFOLIO """
    if short is True:
            short_port = Short_Portfolio(data, noa)
            short_parm = short_port[0]
            short_weights = short_port[1]
            if pie == 1:
                plt.figure(figsize=plt.figaspect(1))
                plt.pie(short_weights, labels=symbols, autopct='%.2f')
                plt.figure()            
    

    print()    
    
    
    """ EFFICIENCY FRONTIER """
    # Optimization settings
    cons = ({'type': 'eq', 'fun': lambda x: pmt.statistics(x, data)[0] - tret},
             {'type': 'eq', 'fun': lambda x: np.sum(x)-1})
    bnds = tuple((0, 1) for x in weights)
    
    # Get min and max for plotting
    min_ret = min(prets)
    max_ret = max(prets)
    
    trets = np.linspace(min_ret, max_ret, 30)
    tvols = []
    
    for tret in trets:
        cons = ({'type': 'eq', 'fun': lambda x: pmt.statistics(x, data)[0] - tret},
                 {'type': 'eq', 'fun': lambda x: np.sum(x)-1})    
        res = sco.minimize(pmt.min_func_port, 
                           noa * [1. / noa,],
                           data,
                           method ='SLSQP', 
                           bounds=bnds, 
                           constraints=cons)
        tvols.append(res['fun'])    
    
    # Convert to array
    tvols = np.array(tvols)


    """ PLOT """
    # Random Portfolio Composition
    plt.scatter(pvols, prets, c=prets / pvols, marker='.')
    
    # Efficient Frontier
    plt.plot(tvols, trets, 'r')
    
    # Highest Sharpe Ratio Portvolio
    plt.plot(max_sr_parm[1], max_sr_parm[0], 'bo', fillstyle='full', markersize=8.0)
    
    # Minimum Variance Portfolio
    plt.plot(min_var_parm[1], min_var_parm[0], 'bo', fillstyle='full', markersize=8.0)
    
    # Current Portfolio
    if current_portfolio is not 0:
        plt.plot(curr_port_parm[1], 
                 curr_port_parm[0], 
                 'ro', fillstyle='full', 
                 markersize=8.0)
    
    # Short Portfolio
    if short is True:
        plt.plot(short_parm[1],
                 short_parm[0],
                 'go', fillstyle='full',
                 markersize=8.0)
    
    # Plotting settings
    plt.grid(True)
    plt.xlabel("Expected Volatility")
    plt.ylabel("Expected Return")
    plt.colorbar(label="Sharpe Ratio")
    plt.title("EFFICIENT FRONTIER")
    plt.ylim(min_ret-0.025, max_ret+0.025)
    plt.figure()
    
    return(max_sr_weights, min_var_weights)    
