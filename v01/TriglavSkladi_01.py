import sys
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind



# Imports data - very simple
def Excel(filepath, sheet, columns_list):
    ReadExcel = pd.read_excel(filepath, sheet)
    df = DataFrame(ReadExcel, columns=columns_list)
    df.dropna(inplace=True)
    print(df.head(), "\n")
    return(df)


# Plot - only to be used in CAAR function! 
def graph(asset, day_list, caar, benchmark="benchmark", beat=1, beat_miss_colors=1, zero_line=1):
    fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)

    if beat == 1:
        ax1.set_title(asset + " vs " +benchmark+ " when beat")
        ax1.plot(day_list, caar, color='blue', label='$CAAR$')
        if zero_line == 1:
            plt.hlines(0, -3, 3, color="black", linestyle="dashed")
    else:
        ax1.set_title(asset + " vs " +benchmark+ " when miss")
        if beat_miss_colors == 1:
            color_miss = "red"
        else:
            color_miss = "blue"
        ax1.plot(day_list, caar, color=color_miss, label='$CAAR$')            
        if zero_line:
            plt.hlines(0, -3, 3, color="black", linestyle="dashed")
    
    ax1.legend(loc='best')
    ax1.set_xlabel('Time Horizon')
    ax1.set_ylabel("CAAR")
    # plt.yticks(np.arange(-0.001,0.001,0.0001))
    plt.figure();


# Aux function for aar in caar
def AAR(data, asset, window_column, day):
    wdw = data.loc[data[window_column] == day, asset]
    a = sum(wdw)
    b = len(wdw)
    c = a/b
    return(c)
  

# Caar for asset in asset list
def CAAR(data, asset_list, window_column, day_list, benchmark, 
         beat=1, beat_miss_colors=1, zero_line=1):
        
    all_caar = []
    for asset in asset_list:
        aar = []                
        for day in day_list:                    
                aar.append(AAR(data, asset, window_column, day))
        
        caar = np.cumsum(aar)
        graph(asset, day_list, caar, benchmark, beat, beat_miss_colors, zero_line)
        all_caar.append(caar)
    return(all_caar)


def pair_graph(beat, miss, asset_list, day_list, benchmark):
    for asset in range(0,len(asset_list)):
        asset_name = asset_list[asset]
        fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
        ax1.set_title(asset_name + " vs " +benchmark)
        
        ax1.plot(day_list, beat[asset], color='blue', label='$beat$')
        plt.hlines(0, -3, 3, color="black", linestyle="dashed")  
        ax1.plot(day_list, miss[asset], color="red", label='$miss$')            
        
        ax1.legend(loc='best')
        ax1.set_xlabel('Time Horizon')
        ax1.set_ylabel("CAAR")
        plt.yticks(np.arange(-0.001,0.001,0.0001))
        plt.figure();





# =============================================================================#    

# SETTINGS - GENERAL
f = '/Users/Alen/Documents/0_Academic/0_University/2_Magistrski_Studij/3_Semester (2018)/Empirical Asset Pricing/2_Trigav Skladi/v01/ts-02.xlsx'
day_list = [-3, -2, -1, 0, 1, 2, 3]
benchmarks = ["CPEXEMUY", "ECCPEMUY", "CPI_CHNG", "CPUPXCHG", "PCE_CMOM"]
asset_list1 = ["IB8A_AR", "QW1A_AR"]
asset_list2 = ['LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR',
               'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR',
               'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR']

window_column1b = "window_beat_CPEXEMUY"
window_column1m = "window_miss_CPEXEMUY"

window_column2b = "window_beat_ECCPEMUY"
window_column2m = "window_miss_ECCPEMUY"

window_column3b = "window_beat_CPI_CHNG"
window_column3m = "window_miss_CPI_CHNG"

window_column4b = "window_beat_CPUPXCHG"
window_column4m = "window_miss_CPUPXCHG"

window_column5b = "window_beat_PCE_CMOM"
window_column5m = "window_miss_PCE_CMOM"


# IMPORT
iimport = 1
if iimport == 1:
    s1b = "1beat"
    c1b = ['Date','IB8A_AR','QW1A_AR', window_column1b]
    b1 = Excel(f, s1b, c1b)
    s1m = '1miss'
    c1m = ['Date','IB8A_AR','QW1A_AR', window_column1m]
    m1 = Excel(f, s1m, c1m)
    
    s2b = "2beat"
    c2b = ['Date','IB8A_AR','QW1A_AR', window_column2b]
    b2 = Excel(f, s2b, c2b)
    s2m = '2miss'
    c2m = ['Date','IB8A_AR','QW1A_AR', window_column2m]
    m2 = Excel(f, s2m, c2m)
    
    s3b = "3beat"
    c3b = ['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR',
                   'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR',
                   'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', window_column3b]
    b3 = Excel(f, s3b, c3b)
    s3m = '3miss'
    c3m = ['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR',
                   'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR',
                   'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', window_column3m]
    m3 = Excel(f, s3m, c3m)
    
    s4b = "4beat"
    c4b = ['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR',
                   'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR',
                   'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', window_column4b]
    b4 = Excel(f, s4b, c4b)
    s4m = '4miss'
    c4m = ['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR',\
                   'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR',\
                   'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', window_column4m]
    m4 = Excel(f, s4m, c4m)
    
    s5b = "5beat"
    c5b = ['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR',\
                   'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR',\
                   'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', window_column5b]
    b5 = Excel(f, s5b, c5b)
    s5m = '5miss'
    c5m = ['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR',\
                   'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR',\
                   'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', window_column5m]
    m5 = Excel(f, s5m, c5m)


# ANALYSIS
analysis = 1
beat_miss_colors = 1
zero_line = 1

if analysis == 1:
    beat1 = CAAR(b1, asset_list1, window_column1b, day_list, benchmarks[0], 1, beat_miss_colors, zero_line)
    miss1 = CAAR(m1, asset_list1, window_column1m, day_list, benchmarks[0], 0, beat_miss_colors, zero_line)
    
    beat2 = CAAR(b2, asset_list1, window_column2b, day_list, benchmarks[1], 1, beat_miss_colors, zero_line)
    miss2 = CAAR(m2, asset_list1, window_column2m, day_list, benchmarks[1], 0, beat_miss_colors, zero_line)
    
    beat3 = CAAR(b3, asset_list2, window_column3b, day_list, benchmarks[2], 1, beat_miss_colors, zero_line)
    miss3 = CAAR(m3, asset_list2, window_column3m, day_list, benchmarks[2], 0, beat_miss_colors, zero_line)
    
    beat4 = CAAR(b4, asset_list2, window_column4b, day_list, benchmarks[3], 1, beat_miss_colors, zero_line)
    miss4 = CAAR(m4, asset_list2, window_column4m, day_list, benchmarks[3], 0, beat_miss_colors, zero_line)
    
    beat5 = CAAR(b5, asset_list2, window_column5b, day_list, benchmarks[4], 1, beat_miss_colors, zero_line)
    miss5 = CAAR(m5, asset_list2, window_column5m, day_list, benchmarks[4], 0, beat_miss_colors, zero_line)


# Paired Graphs
paired_graphs = 1
if paired_graphs == 1:
    pair_graph(beat1, miss1, asset_list1, day_list, benchmarks[0])  
    pair_graph(beat2, miss2, asset_list1, day_list, benchmarks[1])
    pair_graph(beat3, miss3, asset_list2, day_list, benchmarks[2])
    pair_graph(beat4, miss4, asset_list2, day_list, benchmarks[3])
    pair_graph(beat5, miss5, asset_list2, day_list, benchmarks[4])


t1 = ttest_ind(beat1, miss1)
t2 = ttest_ind(beat2, miss2)
t3 = ttest_ind(beat3, miss3)
t4 = ttest_ind(beat4, miss4)
t5 = ttest_ind(beat5, miss5)






''' TO-DO:
    * Shrani slike v pdf znotraj vsakega loopa
'''



# TEST
'''
ΣΑR is the sum of abnormal returns, i.e. CAR. 
Also, N is the number of days in the event window.

TEST= ((ΣAR)/N) / (AR_SD/sqrt(N)) = 
(ΣAR*sqrt(N)) / (N*ΑR_SD) = ΣAR / (sqrt(N)*AR_SD) = (
1/sqrt(number of days in event window)) * ( cumulative_abnormal_return /ar_sd).
'''
## H0: CAAR=0


    

