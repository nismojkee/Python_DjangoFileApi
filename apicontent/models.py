from django.db import models
from datetime import datetime
import xlrd, os
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class File(models.Model):
	fileId = models.AutoField(primary_key=True)
	fileName = models.CharField(max_length=100)
	upload_date = models.DateField()
	processed_date = models.DateField(null = True)
	status = models.CharField(max_length=100)
	result = models.CharField(max_length=200)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.upload_date = datetime.utcnow()
		self.status = 'Uploaded'

	def as_dict(self):
		return {
			'id': self.fileId,
			'upload_date': self.upload_date,
			'processed_date': self.processed_date,
			'status': self.status,
			'result': self.result,
		}

	def process(self):
		file = xlrd.open_workbook(os.path.join(settings.MEDIA_ROOT, '/'.join([self.fileName])))
		self.status = 'Processing'
		ln1 = []
		sum1 = 0
		ln2 = []
		sum2 = 0
		x = []
		xColumn = []
		for sheet in file.sheets():
			for row in range(sheet.nrows):
				for col in range(sheet.ncols):
					if sheet.cell_value(row, col) == 'before':
						ln1 = sheet.col_values(col)
					if sheet.cell_value(row, col) == 'after':
						ln2 = sheet.col_values(col)
					x = list(set(ln1) & set(ln2))
					xColumn = 'before: removed {}'
					sum1 = sum(
						(
							int(ln1[i]) for i in range(
								1,
								int(len(list(filter(None, ln1))))
							)
						)
					)
					sum2 = sum(
						(
							int(ln2[i]) for i in range(
								1,
								int(len(list(filter(None, ln2))))
							)
						)
					)
					if sum1 > sum2:
						xColumn = 'after: added {}'
		self.processed_date = datetime.utcnow()
		self.status = 'Ready'
		self.result = xColumn.format(int(x[0]))
		self.save()



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)