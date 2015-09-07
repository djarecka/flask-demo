import Quandl
import pandas
import pdb

#TODO ticker symbol i miesiace
def monthly_data(ticker_symbol):
    mydata = Quandl.get("WIKI/GOOG", trim_start="2014-08-07", trim_end="2015-09-07")
    
    return 3
