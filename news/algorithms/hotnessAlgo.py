import csv
import time
from datetime import datetime, timedelta
from math import log


epoch = datetime(1970, 1, 1)

def epoch_seconds(date):
    """Returns the number of seconds from the epoch to date."""
    # date=datetime(yy,mm,dd)
    td = date - epoch
    return td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)

def score(ups, downs, clicks):
    return ups*2 + downs*(-1) + clicks*1

def hot(ups, downs, clicks, date, counter):
    if counter == 0:
        print "****************executing hotness algorithm****************"
        
    """The hot formula. Should match the equivalent function in postgres."""
    if str(ups).lower() == 'upvotes':
    	print('errorvalue')
    s = score(int(ups), int(downs), int(clicks))
    order = log(max(abs(s), 1), 10)
    sign = 1 if s > 0 else -1 if s < 0 else 0
    # slist = date.split("-")
    date = date.replace(tzinfo=None)
    # print("slist")
    # print(slist)
    seconds = epoch_seconds(date) - 1199145600  #unix timestamp 01 jan 2008
    return round(sign * order + seconds / 45000, 7)



