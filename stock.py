#!/usr/bin/python

import urllib.request
import sys

def get_info(stock_name):
    """
    Input: stock name
    Return value: last trade date, time, price, P/S ratio, P/E ratio
    """
    #p5= price/sales, r=P/E ratio
    url="http://finance.yahoo.com/d/quotes.csv?s="+stock_name
    url+="&f=d1t1l1p5r"
    page=urllib.request.urlopen(url).read().decode()
    return page.strip().split(",")

def get_history(stock_name, a_year, a_month, a_day, z_year, z_month, z_day):
    """
    arguments: stock name, start year, month, day, end year, month, day
    returns CSV string of stock info from start date to end date
    example:
    get_history("GOOG", 2014, 1, 1, 2014, 8, 5) returns info from
    2014-Jan-1 to 2014-Aug-5
    """
    url="http://real-chart.finance.yahoo.com/table.csv?s="+stock_name
    url+="&c="+str(a_year)+"&a="+str(a_month-1)+"&b="+str(a_day)
    url+="&f="+str(z_year)+"&d="+str(z_month-1)+"&e="+str(z_day)
    csv=urllib.request.urlopen(url).read().decode()
    return csv
