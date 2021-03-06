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

					url(r'^category/(?P<categoryName>[\w\-]+)/$','news.views.category'),

					url(r'^like/(?P<docid>\d+)/(?P<userid>\d+)/$','news.views.like'),
					url(r'^dislike/(?P<docid>\d+)/(?P<userid>\d+)/$','news.views.dislike'),
					url(r'^register/$','news.views.register_user'),
					url(r'^select_categories/$','news.views.select_categories'),
					url(r'^catView/$','news.views.cat'),






					)