import urllib.request
import sys
import xml.etree.ElementTree as ET
from financial_terms import *

extract_words("Financial_terms.csv")

def get_headlines(stock_name):
    """
    Argument: stock_name as string, e.g. "YHOO", "GOOG"
    Return value: list of headlines (strings), from the Yahoo RSS feed
    """
    urls=[]
    urls.append("http://finance.yahoo.com/rss/headline?s="+stock_name)
    urls.append("https://news.google.com/news/feeds?hl=en&q="+stock_name+"&output=rss")
    headlines=[]
    for url in urls:
        page=urllib.request.urlopen(url).read().decode()
        # extract the headlines from the page
        root=ET.fromstring(page)
        channel=root[0]
        for item in channel.findall("item"):
            headlines.append(item.find("title").text)
    return headlines

def get_score(stock_name):
    """
    returns a score based on headlines and financial terms dictionary
    """
    headlines=get_headlines(stock_name)
    return compare_headlines(headlines)/len(headlines)
