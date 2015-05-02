from django.conf.urls import patterns, include, url
from django.views.generic import ListView,DetailView
from news.models import Dataset,Hot


urlpatterns=patterns('',
					#url(r'^$', ListView.as_view(

							#queryset=Articledataset1.objects.all(). order_by("-docid")[:10],
					#		queryset=a,
					#		template_name="hot.html")),
					url(r'^$','news.views.articles'
						),
					url(r'^auth/$','news.views.auth_view'),
					
					url(r'^logout/$','news.views.logout'),


					)