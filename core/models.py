from django.db import models


class Picture(models.Model):
	image = models.ImageField(upload_to='images/%Y/%m/%d/')
	visible = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Images'

	def __str__(self):
		return self.image.path


class BackColor(models.Model):
	color = models.CharField(max_length=16)
	visible = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Background color'
		verbose_name_plural = 'Background colors'

	def __str__(self):
		return self.color

