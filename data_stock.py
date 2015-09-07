import Quandl
import pandas
import datetime


def monthly_data(ticker_symbol, var_list):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    month_ago = datetime.datetime.now().replace(month=datetime.datetime.now().month-1).strftime("%Y-%m-%d")
    # using quandl library to get data for last month
    mydata = Quandl.get("WIKI/"+ticker_symbol, trim_start=month_ago, trim_end=today)

    # creating dict. to write requested features
    data = {}
    for var in var_list:
        data[var] = mydata[var]
    data["time"] = mydata.index
    return data

if __name__ == "__main__":
    data =  monthly_data(ticker_symbol="GOOG")
    print data
