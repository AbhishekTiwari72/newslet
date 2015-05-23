import math
import csv
from news.models import Hot,Dataset,Categories,Info


def execute():
	sheet = list(csv.reader(open('news/csv/articlesDataset2.csv','rU')))
	sheet2 = list(csv.reader(open('news/csv/UserProfiles.csv','rU')))
	yowList = Info.objects.all()

	avgRatingArticle={}
	def ratingCountFunc():
		ratingCount={}
		for row in sheet[1:]:
			ratingCount[int(row[0])]=int(row[10])+int(row[11])+int(row[12])
		return ratingCount

	def ratingSumFunc():
		ratingSum={}
		for row in sheet[1:]:
			ratingSum[int(row[0])]=(1*int(row[10]))+(2*int(row[11]))+(-1*int(row[12]))
		return ratingSum


	def globalAvgFunc(ratingCount,ratingSum):
		totalRatings=0
		sumOfRatings=0
		for key in ratingCount:
			totalRatings+=ratingCount[key]
			sumOfRatings+=ratingSum[key]
			avgRatingArticle[key]=ratingSum[key]/(1.0*ratingCount[key])
		return (sumOfRatings/(1.0*totalRatings))

	def meuFunc(globalAvg,k,ratingCount,ratingSum):
		#Pseudo_avg[movie] =( GlobalAverage * K + RatingSum[movie]) / (K + RatingCount[movie])
		avgArticle={}
		for key in ratingCount:
			avgArticle[key]=(globalAvg*k +ratingSum[key])/(k+ratingCount[key])
		return avgArticle

	def ratingCountUserFunc():
		ratingCountUser={}
		for user in sheet2[1:]:
			userId=int(user[0])
			j=0
			for row in yowList:
				if row.user_id == userId:
					j+=1
			ratingCountUser[userId]=j
		return ratingCountUser

	def userOffsetSumFunc():
		offsetSum={}
		for user in sheet2[1:]:
			userId=int(user[0])
			j=0
			for row in yowList:
				if row.doc_id not in avgRatingArticle:
					continue;
				#print row[23],userId
				if row.user_id==userId:
					#print int(row[20])
					#print int(row[19])
					#print avgRatingArticle[int(row[20])]
					j+=(row.user_like)-avgRatingArticle[row.doc_id]
					#print j
			offsetSum[userId]=j
			
		return offsetSum
			
	def globalUserOffsetFunc(ratingCountUser,userOffsetSum):
		totalOffsets=0
		sumOfOffsets=0
		for key in ratingCountUser:
			totalOffsets+=ratingCountUser[key]
			sumOfOffsets+=userOffsetSum[key]
			
		return (sumOfOffsets/(1.0*totalOffsets))

	def userOffsetFunc(globalUserOffset,k,ratingCountUser,userOffsetSum):
		userOffset={}
		for key in ratingCountUser:
			userOffset[key]=(globalUserOffset*k +userOffsetSum[key])/(k+ratingCountUser[key])
		return userOffset



	#constants taken
	k=25
	lambdaConst=0.001
	gammaConst=0.1



	#calculation of Item Offest
	ratingCount={}
	ratingCount = ratingCountFunc()

	ratingSum={}
	ratingSum = ratingSumFunc()
	globalAvg = globalAvgFunc(ratingCount,ratingSum)

	itemOffest = {}
	itemOffest = meuFunc(globalAvg,k,ratingCount,ratingSum)

	#calculation of User offset
	ratingCountUser = ratingCountUserFunc()

	userOffsetSum=userOffsetSumFunc()


	gobalUserOffset={}
	globalUserOffset=globalUserOffsetFunc(ratingCountUser,userOffsetSum)

	userOffest={}
	userOffest=userOffsetFunc(globalUserOffset,k,ratingCountUser,userOffsetSum)

	featuresCount = 40

	docIdDict = dict()
	row_count = sum(1 for row in sheet)

	for i in range(1,row_count):
		if int(sheet[i][0]) in docIdDict:
			continue
		else:
			docIdDict[int(sheet[i][0])] = 1

	row_count_yow = len(yowList)
	row_count_user = sum(1 for row in sheet2)

	userFeature = {}
	itemFeature = {}

	for i in range(1, row_count_user):
		for t in range(0,featuresCount):
			if int(sheet2[i][0]) in userFeature:
				userFeature[int(sheet2[i][0])].append(0.1)
			else: 
				userFeature[int(sheet2[i][0])] = [0.1]

	for key in docIdDict:
		for t in range(0,featuresCount):
			if key in itemFeature:
				itemFeature[key].append(0.1)
			else: 
				itemFeature[key] = [0.1]

	# print itemFeature[504][0]*userFeature[51][0]


	def dotProduct(user_id, item_id):
		if user_id in userFeature:
			userList = userFeature[user_id]
		else :
			return 0
		if item_id in itemFeature:
			itemList = itemFeature[item_id]
		else: 
			return 0
		mulList = [a*b for a,b in zip(userList,itemList)]
		sumValue = (sum(mulList))
		return sumValue

		# print sum(mulList)

	j = 0

	countArticle = 0
	meanError = 0.0

	# print docIdDict[504]
	diff = 1000000.0
	for i in range(0,featuresCount):
		
		print "k=",i
		for j in range(0,120):
			# if j >= 2 and (diff < 0.002 or diff > -0.002): 
			# 	print "break"
			# 	break
			# else:
			sse=0
			n=0
			for p in range(1,row_count_yow):
				
				if yowList[p].doc_id in docIdDict:

					item_id = yowList[p].doc_id
					user_id = yowList[p].user_id
					rating = yowList[p].user_like

					prediction = userOffest[user_id] + itemOffest[item_id] +dotProduct(user_id,item_id)
					currError = rating-prediction
					sse+=currError**2
					n+=1
					userf =  userFeature[user_id][i]
					itemf = itemFeature[item_id][i]
					# print userf
					userFeature[user_id][i] += lambdaConst*(currError*itemf - gammaConst*userf)
					itemFeature[item_id][i] += lambdaConst*(currError*userf - gammaConst*itemf)
					
					
					
			meanError = math.sqrt(sse/n)

			
			
			if abs(diff-meanError)<0.0001:
				break;
			diff = meanError
			print "epoch=",j
			print "error=",meanError
			
			


	# print userFeature

	itemFeatureTranspose = {}

	rowItems =  len(itemFeature)

	for key in itemFeature:
		for f in range(0,featuresCount):
			if f in itemFeatureTranspose:
				itemFeatureTranspose[f].append({'key' : key, 'keyValue': itemFeature[key][f]})
			else:
				itemFeatureTranspose[f] = [{'key' : key ,'keyValue' : itemFeature[key][f]}]

	predictionMatrix = {}


	for key1 in userFeature:
		for i in range(0,rowItems):
			netVal = 0.0
			for l in range(0,featuresCount):
				val1 = userFeature[key1][l]
				val2 = itemFeatureTranspose[l][i]['keyValue'] 
				netVal += val1*val2
				item_id = itemFeatureTranspose[l][i]['key']
			if key1 in predictionMatrix:
				predictionMatrix[key1].append({'item_id' : item_id, 'value' : netVal})
			else:
				predictionMatrix[key1] = [{'item_id' : item_id, 'value' : netVal}]


	fCollab = open('news/csv/funkSVD.csv','wb')
	fCollab = csv.writer(fCollab)


	data = []
	data.append('')
	dataRow = []
	counter = 0
	for key in predictionMatrix:
		if counter == 0:
			for i in range(0,len(predictionMatrix[key])):
				data.append(predictionMatrix[key][i]['item_id'])
		else:
			break
		counter += 1

	dataRow.append(data)
	data = []

	for key in predictionMatrix:
		data.append(key)
		for i in range(0,len(predictionMatrix[key])):
			data.append(predictionMatrix[key][i]['value'])
		dataRow.append(data)
		data = []

	fCollab.writerows(dataRow)

	print len(predictionMatrix[51])









