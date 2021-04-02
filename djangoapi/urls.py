from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apicontent.urls')),
    path('admin/', admin.site.urls),
]
