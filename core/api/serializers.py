from rest_framework import serializers

from core.models import Picture, BackColor


class PictureSerializer(serializers.ModelSerializer):

	class Meta:
		fields = '__all__'
		model = Picture


class BackColorSerializer(serializers.ModelSerializer):

	class Meta:
		fields = '__all__'
		model = BackColor