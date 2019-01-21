import numpy as np
import pandas as pd 
from pandas import DataFrame
from scipy.stats import linregress


# get_indexer_for ... gets index numbers if condition is met


def diff(li_bigger, li_smaller):
    return [x for x in li_bigger if x not in li_smaller]



def EstimationWindow(data, n=3, dummy=1):
    s = data.event.eq(dummy)
    dummies = s[s].index
    output=[]
    ind_to_drop = (dummies + n).union(dummies).union(dummies - n)
    c = data.event.cumsum().drop(ind_to_drop)
    for _, g in data.drop(ind_to_drop).groupby(c):
        output.append(g)
    return(output)
    
    
    
def EventWindow (data, n=3, dummy=1, fragment=True):
    '''
    data....data. Contains ALL data - reurns, and event dummies = event column
    dummy...event=1
    n.......days before/after
    '''
    
    idx = data.index.get_indexer_for(data[data.event==dummy].index)
    event_window = data.iloc[np.unique(np.concatenate([np.arange(max(i-n,0), min(i+n+1, len(data)))
                                                    for i in idx]))]
    if fragment==True:
        n*=2
        n+=1
        event_window = [event_window[i:i+n] for i in range(0,event_window.shape[0],n)]
    return(event_window)



def Excel(f):
    data = pd.read_excel(f)
    data.columns = data.columns.str.strip() 
    data.dropna(inplace=True)
    data.reset_index(drop=True, inplace=True)
    print(data.head())
    return(data)

def Excel2 (path, filename, sheets, columns_list, skiprows=1, header=None):
    ReadExcel = pd.read_excel(path+filename, sheets, skiprows=skiprows, header=header)
    df = DataFrame(ReadExcel, columns=columns_list)
#    df.columns = df.columns.str.strip() 
    df.dropna(inplace=True)
    print(df.head(), "\n")
    return(df)

def Excel3 (path, filename, sheet, column_names, cols_to_del):
    xl = pd.ExcelFile(path+filename)
    df = xl.parse(sheet, header=None, names=column_names)
    df.drop(df.columns[cols_to_del] , axis=1, inplace=True)
    return(df)



def CAPM (estimation_window, benchmark, assets):
    alpha = []
    beta = []    
    for i, df in enumerate(estimation_window):
        alpha.append([])
        beta.append([])            
        for ass in assets:
            slope, intercept, r_value, p_value, std_err = linregress(estimation_window[i][benchmark],
                                                                     estimation_window[i][ass])
            alpha[i].append(intercept)
            beta[i].append(slope)
    return(alpha, beta)
    
   
    
def AbnormalReturns (CAPM_results, event_window, assets, benchmark):
    abnormal_returns = []
    for asset in range(len(assets)): #2
        abnormal_asset = []    
        abnormal_event = []
        for event in range(len(event_window)):
            
            alpha = CAPM_results[0][event][asset]
            beta = CAPM_results[1][event][asset]
            bench = event_window[event][benchmark]
            name = assets[asset]
            val = event_window[event][name]
    
            ar1 = [j - alpha for j in val]
            ar2 = [j * beta for j in bench]
            ar3 = [x1 - x2 for (x1, x2) in zip(ar1, ar2)]
            abnormal_event.append(ar3)
            
        abnormal_asset.append(abnormal_event)
        abnormal_returns.append(abnormal_asset)
    return(abnormal_returns)
    
    
    

def graph(asset, day_list, caar, days, benchmark="benchmark", beat=1, beat_miss_colors=1, zero_line=1):
    import matplotlib.pyplot as plt
    
    fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)

    if beat == 1:
        ax1.set_title(asset + " vs " +benchmark+ " when beat")
        ax1.plot(day_list, caar, color='blue', label='$CAAR$')
        if zero_line == 1:
            plt.hlines(0, -days, days, color="black", linestyle="dashed")
    else:
        ax1.set_title(asset + " vs " +benchmark+ " when miss")
        if beat_miss_colors == 1:
            color_miss = "red"
        else:
            color_miss = "blue"
        ax1.plot(day_list, caar, color=color_miss, label='$CAAR$')            
        if zero_line:
            plt.hlines(0, -days, days, color="black", linestyle="dashed")
    
    ax1.legend(loc='best')
    ax1.set_xlabel('Time Horizon')
    ax1.set_ylabel("CAAR")
    # plt.yticks(np.arange(-0.001,0.001,0.0001))
    plt.figure();
    
    
