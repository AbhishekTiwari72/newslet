# Create your views here.
from django.shortcuts import render, get_object_or_404
from news.models import Hot,Dataset
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def articles(request):
	# get the blog posts that are published
	session_user="none"
	session_password="none"
	if 'username' in request.session:
		session_user=request.session['username']
		session_password=request.session['password']
	
	s=Hot.objects.all().order_by("-hottness")[:10]
	
	list2=list()
	for i in range(0,10):
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
		print list2
		c={}
		c.update(csrf(request))

		
	return render (request,'index.html',{'username':session_user,'password':session_password,'list2':list2})

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
def logout(request):
	auth.logout(request)
	request.session['username']="none"
	request.session['password']="none"
	return HttpResponseRedirect('/news/')

