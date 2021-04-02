from django.conf.urls import url
from django.urls import path
from apicontent import views
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
	path('login', obtain_auth_token, name = "login"),
	url(r'^file/savefile$', views.fileUpload)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
