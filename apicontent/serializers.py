from rest_framework import serializers
from apicontent.models import File

class FileSerializer(serializers.Serializer):
	class Meta:
		model = File
		fields = (
			'fileId',
			'fileName',
			'upload_date',
			'processed_date',
			'status',
			'result'
		)
