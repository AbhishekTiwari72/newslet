from celery import task
import csv
import time
from datetime import datetime, timedelta
from math import log
from algorithms import *
from news.models import Hot,Dataset,Categories,Info


@task()
def add(x, y):
    return x + y


@task()
def hotness():
	sheet = list(csv.reader(open('news/csv/articlesDataset2.csv','rU')))
	sheet2 = open('news/csv/hotnessData.csv', 'wb')
	a = csv.writer(sheet2)
	a.writerow(['docid', 'date', 'hottness'])
	for row in sheet[1:]:
	    hottnessVal = hotnessAlgo.hot(row[11], row[12], row[10], row[6])
	    hotObj = Hot.objects.get(docid=int(row[0]))
	    hotObj.hottness = hottnessVal
	    hotObj.save()
	    a.writerow([row[0], row[6], hottnessVal])
	sheet2.close()
	return "suscess"

@task()
def funk():
	funkSVDnew.execute()
	return "funk success"


@task()
def contentBased():
	vectorBased.execute()
	userProfile.execute()
	vectorBasedProduct.execute()
	return "contentSuccess"