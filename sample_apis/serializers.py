__author__ = 'gwjang'
from django.forms import widgets
from rest_framework import serializers
from sample_apis.models import Snippet, SampleImage, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class SampleImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = SampleImage
		fields = ('title', 'url')