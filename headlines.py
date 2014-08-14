import urllib.request
import sys
import xml.etree.ElementTree as ET

def get_history(stock_name):
    """
    Argument: stock_name as string, e.g. "YHOO", "GOOG"
    Return value: list of headlines (strings), from the Yahoo RSS feed
    """
    url="http://finance.yahoo.com/rss/headline?s="+stock_name
    page=urllib.request.urlopen(url).read().decode()
    # extract the headlines from the page
    root=ET.fromstring(page)
    channel=root[0]
    headlines=[]
    for item in channel.findall("item"):
        headlines.append(item.find("title").text)
    return headlines
