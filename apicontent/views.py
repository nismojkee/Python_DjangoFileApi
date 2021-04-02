from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
import threading

from apicontent.models import File
from apicontent.serializers import FileSerializer

@csrf_exempt
def fileUpload(request):
	file = request.FILES['uploadedFile']
	file_name = default_storage.save(file.name, file)
	fileUpload = File(
		fileName = file_name
	)
	fileUpload.save()
	response = JsonResponse(fileUpload.as_dict())
	response.status_code = 201
	thread = threading.Thread(fileUpload.process())
	thread.start()
	return JsonResponse(file_name, safe = False)
