# coding=utf-8
import os

"""
Goal: Downloading financial data (related to stock markets) from diverse sources
      (Alpha Vantage, Yahoo Finance).
Authors: Thibaut Théate and Damien Ernst
Institution: University of Liège
"""

###############################################################################
################################### Imports ###################################
###############################################################################

import pandas as pd
import pandas_datareader as pdr
import requests
import os
import pandas as pd
import yfinance as yf
from io import StringIO




###############################################################################
########################### Class YahooFinance ################################
###############################################################################

class YahooFinance:   
    """
    GOAL: Downloading stock market data from the Yahoo Finance API. See the
          pandas.datareader documentation for more information.
    
    VARIABLES:  - data: Pandas dataframe containing the stock market data.
                                
    METHODS:    - __init__: Object constructor initializing some variables.
                - getDailyData: Retrieve daily stock market data.
                - processDataframe: Process a dataframe to homogenize the
                                    output format.
    """
    

    def __init__(self):
        """
        GOAL: Object constructor initializing the class variables. 
        
        INPUTS: /      
        
        OUTPUTS: /
        """
        
        self.data = pd.DataFrame()

    
    def getDailyData(self, marketSymbol, startingDate, endingDate):
        """
        GOAL: Downloding daily stock market data from the Yahoo Finance API. 
        
        INPUTS:     - marketSymbol: Stock market symbol.
                    - startingDate: Beginning of the trading horizon.
                    - endingDate: Ending of the trading horizon.
          
        OUTPUTS:    - data: Pandas dataframe containing the stock market data.
        """
        
      
    
        try:
            # data = pdr.data.DataReader(marketSymbol, 'yahoo', startingDate, endingDate)
            stock = yf.Ticker(marketSymbol)
            data = stock.history(start=startingDate, end=endingDate)
            self.data = self.processDataframe(data)
            print(f'Length of the datframe: {len(self.data)}')
            return self.data
        except Exception as e:
            print(f"An error occurred while fetching data from Yahoo Finance: {e}")
            # Handle the error or return an empty DataFrame
        return pd.DataFrame()


    def processDataframe(self, dataframe):
        """
        GOAL: Process a downloaded dataframe to homogenize the output format.
        
        INPUTS:     - dataframe: Pandas dataframe to be processed.
          
        OUTPUTS:    - dataframe: Processed Pandas dataframe.
        """
        
        # Adapt the dataframe index and column names
        dataframe.index.names = ['Date']
        dataframe = dataframe[['Open', 'High', 'Low', 'Close', 'Volume']]

        return dataframe


    
###############################################################################
############################# Class CSVHandler ################################
###############################################################################
    
class CSVHandler:
    """
    GOAL: Converting "Pandas dataframe" <-> "CSV file" (bidirectional).
    
    VARIABLES: /
                                
    METHODS:    - dataframeToCSV: Saving a dataframe into a CSV file.
                - CSVToDataframe: Loading a CSV file into a dataframe.
    """
    
    
    def dataframeToCSV(self, name, dataframe):
        """
        GOAL: Saving a dataframe into a CSV file.
        
        INPUTS:     - name: Name of the CSV file.   
                    - dataframe: Pandas dataframe to be saved.
          
        OUTPUTS: /
        """


        directory = os.path.dirname(name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        path = name + '.csv'
        dataframe.to_csv(path)
        print(f"Saved the dataframe at {path}")
        
        
        
    def CSVToDataframe(self, name):
        """
        GOAL: Loading a CSV file into a dataframe.
        
        INPUTS:     - name: Name of the CSV file.   
          
        OUTPUTS:    - dataframe: Pandas dataframe loaded.
        """
        
        path = name + '.csv'
        # Attempt to read the CSV file without setting an index first
        dataframe = pd.read_csv(path, header=0)

        # Check if 'Timestamp' column exists
        if 'Date' in dataframe.columns:
            dataframe.set_index('Date', inplace=True)
            dataframe.index = pd.to_datetime(dataframe.index)
        else:
            print(f"'Date' column not found in {path}")

        return dataframe