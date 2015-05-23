import csv
from news.models import Hot,Dataset,Categories,Info

def execute():
	tags = list(csv.reader(open('news/csv/TagsProfile.csv','rU')))
	df = list(csv.reader(open('news/csv/DocumentFrequency.csv','rU')))
	userf = list(csv.reader(open('news/csv/UserProfiles.csv','rU')))

	data = []
	# data.append('')
	dataRow = []
	for row in tags:
		data.append(row[0])
	dataRow.append(data)

	columnCount = len(df[0])

	for user in userf[1:]:
		data = []
		data.append(user[0])
		for row in tags[1:]:
			prediction = 0.0
			for i in range (1,columnCount):
				if int(df[1][i]) != 0:
					prediction += float(user[i])*(1/float(df[1][i]))*float(row[i])
			data.append(prediction)
		dataRow.append(data)

	vf = open('news/csv/VectorBased.csv','wb')
	vf = csv.writer(vf)
	vf.writerows(dataRow)




