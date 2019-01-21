# -*- coding: utf-8 -*-
from __future__ import print_function

__version__ = "0.0.06"
__author__ = "Alen Rozac"

"""
Copyright 2018 Alen Rozac

Licensed under the GNU Lesser General Public License, v3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.gnu.org/licenses/lgpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import pyfolio_tools as pft
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

#  IMPORT Google Sheets data
# 'https://docs.google.com/spreadsheets/d/1CUA5MIlGW4aV7IUj_13Qn3RqcvmKeRYOjOtDHVu2aKM/edit#gid=1935084128'
def G_SheetsImport(link, worksheet):
    """ Imports data from Google Sheets sheet. 
    
    ! REQUIRES credentials.json IN WORKING DIRECTORY !
    ! All imported data is defined as STRING. !
    
    ___PARAMETERS
    link: Google Sheets URL
    worksheet: Sheet that is to be imported. Data from A1 to x.
    ___OUTPUT:
    data: Imported data table.    
    """
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(link)
    worksheet = sheet.get_worksheet(worksheet)
    data = worksheet.get_all_values()
    del scope
    return(data)
    

# DOWNLOAD data given tickers, dates.
def DownloadData(symbols, start_date, end_date=0, dropna=1, source='yahoo', metric='Adj Close'):
        """ Returns DataFrame with selected metric for given tickers and dates.
        ___PARAMETERS
        Symbols: List of tickers in YahooFinance format (TICK.EX)
        Start_date: YYYY/MM/DD format; YahooF will select earliest possible dates in cases when start<data
        end_date=0: TODAY is used; can be specified YYYY/MM/DD
        dropna=1: Drops data for other tickers if one ticker has n/a.
        source: Select source (see web_datareader)
        metric: Select metric (see web_datareader)
        ___OUTPUT
        data: Pandas DataFrame with selected metric. MxN. M-dates, N-tickers. 
        """
        import datetime
        import fix_yahoo_finance as yf
        
        yf.pdr_override()        
        print("\nSelected portfolio:", symbols)
        print("Starting download protocol...")
        data = pd.DataFrame()
        if end_date == 0:
            end_date = datetime.datetime.today().strftime('%Y-%m-%d')        
        data = yf.download(symbols, data_source=source, start=start_date, end=end_date,retry_count=15)[metric]
        if dropna == 1:    
            data = data.dropna()
        return(data)
        

# CALCULATE INDEX, and PLOT
def Index(data, graph=1):
    """ Calculates and returns dataframe as index values, starting at date 0
    ___PARAMETERS:
    data: values dataframe (see DownloadData)
    graph=1: Plots the prices, all tickers start at 100.
    """
    
    start_date = str(data.index[0])[:10]
    print("Index base = ", start_date)
    index = data/data.iloc[0]*100
    if graph == 1:
        index.plot()
        plt.title("Index Plot")
        plt.figure()
    return(index)


# CURRENT PORTFOLIO
def TotalInvestment(g_data):
    g_data["investment"] = pd.to_numeric(g_data["investment"])
    total_investment = g_data.investment.sum()
    print()
    print("Total investment (EUR) = ", total_investment)
    return(total_investment)


# Log Returns
def LogReturns(data):
    log_returns = pft.LogReturns(data)
    return log_returns


# Mean Returns (%)
def MeanReturns(data, year=252):
    """ Calculates logarithmic mean values for given data (Pandas DataFrame)
    ___PARAMETERS:
    data: Pandas DataFrame with prices (see DownloadData)
    year=252: Financial year has 252 working days. Can be changed to 360/365/*
    ___OUTPUT:
    mean_returns: Vector of mean returns (log)
    """
    
    print("\nMean Returns log:")
    log_returns = pft.LogReturns(data)
    mean_returns = log_returns.mean()*year
    print(mean_returns)
    return(mean_returns)


# Variance-Covariance Matrix
def VarCov(data, heatmap=1, year=252):
    """ Calculates and displays variance and covariance of input data
    ___PARAMETERS:
    data: Pandas DataFrame with prices (see DownloadData)
    year=252: Financial year has 252 working days. Can be changed to 360/365/*
    ___OUTPUT:
    var_cov: Variance-Covariance Matrix    
    """
    print("\nVariance-Covariance Matrix:")
    log_returns = pft.LogReturns(data)
    var_cov = log_returns.cov()*year
    print(var_cov)
    if heatmap == 1:
        mask = np.zeros_like(var_cov, dtype=np.bool)
        mask[np.triu_indices_from(mask, k=1)] = True
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        sns.heatmap(var_cov, 
                    mask=mask, cmap=cmap, vmax=.9, vmin=-.07, center=0,
                    square=True, linewidths=.5, 
                    cbar_kws={"shrink": .5},
                    annot=True, fmt='.2f')
        plt.yticks(rotation=0)
        plt.title("Variance-Covariance Matrix Heatmap")
        plt.figure()
    return(var_cov)


# PRINT STATS & NORMALITY TESTS
def PrintStatistics(data):
    """ Prints statistics for every ticker.
    """     
    for column in data:
        pft.print_statistics(data[column])
        
def NormalityTest(data):
    """ Prints normality tests for every ticker.
    """      
    for column in data:
        pft.normality_test(data[column])


# LOG RETURNS HISTOGRAM
def ReturnsHistogram(data):
    log_returns = pft.LogReturns(data)
    log_returns.hist(bins=100)
    plt.title("Returns Histogram")
    plt.figure()
    
    
# PRINT ASSET NAMES OF PORTFOLIO
def PrintNames(g_data):
    print(50 * "_")
    print("\nSELECTED PORTFOLIO:" )
    for index, row in g_data.iterrows():
        print(row["ticker"],"\t", row["name"])
    print(50 * "_")
    print()


# Get PORTFOLIO WEIGHTS
def PortfolioWeights(g_data, names=1, pie=1):
    g_data["investment"] = g_data["investment"].astype(float)
    g_data["weight"] = g_data.investment / g_data.investment.sum()
    port_weights = pd.DataFrame(g_data["weight"].values,
                                index = g_data["name"], 
                                columns = ["weights"])
    print("\nCurrent Portfolio Weights:")
    print(port_weights)
    # Plot pie portfolio chart    
    if pie==1:
        plt.figure(figsize=plt.figaspect(1))
        plt.pie(g_data["weight"], labels=g_data["ticker"], autopct='%.2f')
        plt.title("Current Portfolio Composition")
        plt.figure()
    return(port_weights)








# =============================================================================
#  WRAPPERS
# =============================================================================

def Wrapper_Markowitz(data, noa, short=True, current_portfolio=0, pie=1, simulations=2000):
    import pyfolio_markowitz as pfm
    w = pfm.Wrapper_Markowitz_gData(data, noa, pie, simulations, 
                                current_portfolio, short)
    return(w)

    


# =============================================================================
#  GOOGLE WRAPPERS    
# =============================================================================

def Wrapper_G_GetData(g_sheets_link, sheet, start_date, end_date=0, dropna=1):           
        df = G_SheetsImport(g_sheets_link, sheet)
        g_data = pd.DataFrame(df, columns=df[0]) #row0 = col_names
        g_data = g_data.drop(g_data.index[0]) #drop row0 (names)
        symbols = list(g_data["symbol"])        
        data = DownloadData(symbols, start_date, dropna=1, end_date=end_date)
        end_date = str(data.index[-1])[:10]
        noa = len(symbols)
        return g_data, data, symbols, noa, symbols, start_date, end_date



def Wrapper_G_Markowitz(g_sheets_link, sheet, start_date, simulations=3000):
    # Get data from Google Sheet
    p = Wrapper_G_GetData(g_sheets_link, sheet, start_date)
    # Get weights
    portfolio_weights = PortfolioWeights(p[0])
    # Perform Full Markowitz
    Wrapper_Markowitz(p[1], p[3], current_portfolio=portfolio_weights["weights"])
   

    
    