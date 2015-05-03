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

					url(r'^login/$','news.views.login'),
					
					url(r'^logout/$','news.views.logout'),

					url(r'^about/$','news.views.about'),

					url(r'^page/$','news.views.page'),

					url(r'^contact/$','news.views.contact'),

					url(r'^(?P<docid>\d+)/$','news.views.article'),







					)