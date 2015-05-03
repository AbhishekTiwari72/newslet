from django.contrib import admin
from news.models import Dataset,Hot,Info,Categories
from django.contrib.auth.models import User

admin.site.register(Dataset)
admin.site.register(Hot)
admin.site.register(Info)
admin.site.register(Categories)


