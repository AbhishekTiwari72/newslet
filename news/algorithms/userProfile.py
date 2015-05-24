import csv
from news.models import Hot,Dataset,Categories,Info


def execute():
	yowList = Info.objects.all()
	users=[]
	for row in yowList:
		if row.user_id not in users:
			users.append(row.user_id)
	# print users
	x=["userId"]
	sheet2=list(csv.reader(open('news/csv/TagsProfile.csv','rU')))
	columnCount = len(sheet2[0])

	tagsCount = dict()
	for row in sheet2[1:]:
		for q in range(1,columnCount):
			if int(row[q]) == 1: 
				if int(row[0]) in tagsCount:
					tagsCount[int(row[0])] += 1
				else:
					tagsCount[int(row[0])] = 1
	 
	# print tagsCount[504]
	sheet4=open('news/csv/UserProfiles.csv','wb')
	a = csv.writer(sheet4)
	a.writerow(x + sheet2[0][1:])
	for user in users:
		userId=user
		upvotedArticles=[]
		downvotedArticles=[]
		clickedArticles=[]
		for row in yowList:
			if row.user_id==userId:
				if row.user_like== -1:
					downvotedArticles.append(row.doc_id)
				elif row.user_like==1:
					clickedArticles.append(row.doc_id)
				else:
					upvotedArticles.append(row.doc_id)

		userProfile=[]
		userProfile.append(userId)
		for i in range(1,columnCount):
			j=0.0
			for row in sheet2[1:]:
				#print row[0]
				if int(row[0]) in upvotedArticles:
					rating=2
				elif int(row[0]) in downvotedArticles:
					rating=-1
					#print row[0]
				elif int(row[0]) in clickedArticles:
					rating=1
				else:
					continue
				if row[i]=="1": 
					# splitClasses=row[8].split("|")
					#print len
					noOfClasses= tagsCount[int(row[0])]
					j=j+(1/float((noOfClasses**(0.5))))*rating
			userProfile.append(j)
		# print userProfile
		a = csv.writer(sheet4)
		a.writerow(userProfile)