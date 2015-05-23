from django.contrib import admin
from news.models import Dataset,Hot,Info,Categories
from django.contrib.auth.models import User
from kombu.transport.django import models as kombu_models


admin.site.register(kombu_models.Message)
admin.site.register(Dataset)
admin.site.register(Hot)
admin.site.register(Info)
admin.site.register(Categories)


