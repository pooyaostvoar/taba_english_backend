from django.contrib.auth.models import User
from rest_framework import serializers

class UserAuthSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(max_length=200)
