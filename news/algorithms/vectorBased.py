import urllib2
import urllib
import json
import csv
import time
import requests
import math
from news.models import Hot,Dataset,Categories,Info

def execute():
    print "****************executing contentBased****************"
    openDataset = list(csv.reader(open('news/csv/articlesDataset2.csv', 'rU')))
    row_count2 = sum(1 for row in openDataset)
    tagDict = dict()

    newparts = []
    for i in range(1, row_count2):
        string = openDataset[i][8]
        parts = string.split('|')
        parts = filter(None, parts)
        # if i == 1:
        #     print parts
        parts = set(parts)
        for part in parts:
            if part in tagDict:
                tagDict[part] += 1
            else:
                tagDict[part] = 1
        newparts = newparts + list(parts)
        # if i < 10:
        #     print newparts
        newparts = set(newparts)
        newparts = list(newparts)


    import operator
    sorted_x = sorted(tagDict.items(), key=operator.itemgetter(1), reverse=True)
    # print sorted_x[0][1]

    data = []
    data.append('')
    dataRow = []
    frequency = []
    frequency.append('frequency')
    for i in range(0,len(sorted_x)):
        if int(sorted_x[i][1]) >= 20:
            data.append(sorted_x[i][0])
            frequency.append(sorted_x[i][1])
        else:
            break

    dfData = data
    dfDataRow = []
    dfDataRow.append(dfData)
    dfDataRow.append(frequency)
    dataRow.append(data)

    for j in range(1, row_count2):
        data = []
        data.append(int(openDataset[j][0]))
        for k in range(0,i):
            if sorted_x[k][0] in openDataset[j][8]:
                data.append(1)
            else:
                data.append(0)
        dataRow.append(data)

    fTagsProfile = open('news/csv/TagsProfile.csv', 'wb')
    fTagsProfile = csv.writer(fTagsProfile)
    fTagsProfile.writerows(dataRow)


    fDf = open('news/csv/DocumentFrequency.csv', 'wb')
    fDf = csv.writer(fDf)
    fDf.writerows(dfDataRow)