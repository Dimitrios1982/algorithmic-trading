from statsmodels.regression.rolling import RollingOLS 
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt
import  statsmodels.api as sm
import  pandas_datareader.data as web
import  datetime as dt
import  yfinance as yf
import  pandas_ta
import  warnings
warnings.filterwarnings("ignore")

pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')