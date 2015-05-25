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

	sheet = Dataset.objects.all()
	sheet2 = open('news/csv/hotnessData.csv', 'wb')
	a = csv.writer(sheet2)
	a.writerow(['docid', 'date', 'hottness'])
	counter = 0
	for row in sheet:
	    hottnessVal = hotnessAlgo.hot(row.clicks, row.upvotes, row.downvotes, row.published, counter)
	    hotObj = Hot.objects.get(docid=row.docid)
	    hotObj.hottness = hottnessVal
	    hotObj.save()
	    a.writerow([row.docid, row.published, hottnessVal])
	    counter += 1
	sheet2.close()
	return "****************hotness algorithm suscessfully executed****************"

@task()
def funk():
	# userProfile.execute()
	funkSVDnew.execute()
	return "****************funkSVD successfully executed****************"


@task()
def contentBased():
	vectorBased.execute()
	userProfile.execute()
	vectorBasedProduct.execute()
	return "****************contentBased successfully executed****************"