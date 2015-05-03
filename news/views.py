# Create your views here.
from django.shortcuts import render, get_object_or_404
from news.models import Hot,Dataset,Categories,Info
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
import csv

def articles(request):
	# get the blog posts that are published
	session_user="none"
	session_password="none"

	sheet = list(csv.reader(open('/home/gauravgupta/Desktop/BTP/newslet/news/csv/VectorBased.csv','rU')))

	if 'username' in request.session and request.session['username'] != "" and request.session['username'] != "none" :
		session_user=request.session['username']
		session_password=request.session['password']
		# print session_user
		userDocs = Info.objects.filter(user_id=int(session_user))
		flag = 0
		for row in sheet[1:]:
			if int(row[0]) == int(session_user):
				docs = zip(sheet[0][1:],row[1:])
				docs = sorted(docs,key=lambda l:l[1], reverse=True)
				flag = 1
				break
		firstTen = []
		if flag == 1:
			j = 10
			i = 0
			print userDocs.count()
			pp = userDocs.filter(doc_id=215)
			print pp.count()
			while i < j:
				# print i
				findSame = userDocs.filter(doc_id=int(docs[i][0]))
				if findSame.count() > 0:
					j+=1
				else:
					firstTen.append(docs[i])
				i += 1

			vector = []
			for i in range(0,len(firstTen)):
				l =  Dataset.objects.filter(docid=int(firstTen[i][0]))
				list1=list()
				for x in l:
					list1.append(x.docid)
					list1.append(x.headline)
					list1.append(x.trailText)
					list1.append(x.byline)
					list1.append(x.body)
					list1.append(x.webURL)
					list1.append(x.published)
					list1.append(x.imageLink)
					list1.append(x.tags)
					list1.append(x.section)
					list1.append(x.clicks)
					list1.append(x.upvotes)
					list1.append(x.downvotes)
					
				vector.append(list1)
				# print list2
				c={}
				c.update(csrf(request))
		# print "printing ------------------------------------"
		# print firstTen

	
	s = Hot.objects.all().order_by("-hottness")[:15]
	cat = Categories.objects.all().order_by("-occurences")
	
	list2=list()
	for i in range(0,15):
		l=Dataset.objects.filter(docid=s[i].docid)
		list1=list()
		for x in l:
			list1.append(x.docid)
			list1.append(x.headline)
			list1.append(x.trailText)
			list1.append(x.byline)
			list1.append(x.body)
			list1.append(x.webURL)
			list1.append(x.published)
			list1.append(x.imageLink)
			list1.append(x.tags)
			list1.append(x.section)
			list1.append(x.clicks)
			list1.append(x.upvotes)
			list1.append(x.downvotes)
			
		list2.append(list1)
		# print list2
		c={}
		c.update(csrf(request))

	if session_user != "none" and  session_user != "":
		return render(request, 'user.html', {'username': session_user, 'categories' : cat, 'list2' : vector, 'popular': list2 })
	else:	 
		return render (request,'index.html',{'username':session_user, 'categories' : cat,'list2':list2})

def auth_view(request):
	username=request.POST.get('username','')   
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password )
	if user is not None:
		auth.login(request, user)
		request.session['username']=request.user.username
		request.session['password']=request.user.password
		return HttpResponseRedirect('/news/')
	else:
		return HttpResponseRedirect('/blog/invalid')

def login(request):
	if 'username' in request.session and request.session['username'] != "none" and request.session['username'] != "" :
		return HttpResponseRedirect('/news/')
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	request.session['username']="none"
	request.session['password']="none"
	return HttpResponseRedirect('/news/')

def about(request):
	return render(request, 'about.html')

def page(request):
	return render(request,'page.html')

def article(request, docid = 504):
	session_user="none"
	session_password="none"

	if 'username' in request.session and request.session['username'] != "" and request.session['username'] != "none" :
		session_user=request.session['username']
		session_password=request.session['password']

	l = Dataset.objects.filter(docid=docid)
	newsArticle = list()
	for x in l:
		newsArticle.append(x.docid)
		newsArticle.append(x.headline)
		newsArticle.append(x.trailText)
		newsArticle.append(x.byline)
		newsArticle.append(x.body)
		newsArticle.append(x.webURL)
		newsArticle.append(x.published)
		newsArticle.append(x.imageLink)
		newsArticle.append(x.tags)
		newsArticle.append(x.section)
		newsArticle.append(x.clicks)
		newsArticle.append(x.upvotes)
		newsArticle.append(x.downvotes)
	# print newsArticle

	s = Hot.objects.all().order_by("-hottness")[:15]
	cat = Categories.objects.all().order_by("-occurences")
	
	list2=list()
	for i in range(0,15):
		l=Dataset.objects.filter(docid=s[i].docid)
		list1=list()
		for x in l:
			list1.append(x.docid)
			list1.append(x.headline)
			list1.append(x.trailText)
			list1.append(x.byline)
			list1.append(x.body)
			list1.append(x.webURL)
			list1.append(x.published)
			list1.append(x.imageLink)
			list1.append(x.tags)
			list1.append(x.section)
			list1.append(x.clicks)
			list1.append(x.upvotes)
			list1.append(x.downvotes)
			
		list2.append(list1)
		# print list2
		c={}
		c.update(csrf(request))

	if session_user != "none" and  session_user != "":
		return render(request, 'article.html', {'username': session_user, 'article': newsArticle, 'popular': list2 })
	else:	 
		return HttpResponseRedirect('/news/')


def contact(request):
	return render(request, 'contact.html')

