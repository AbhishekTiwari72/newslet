from django.contrib import admin
from news.models import Dataset,Hot
from django.contrib.auth.models import User

admin.site.register(Dataset)
admin.site.register(Hot)
