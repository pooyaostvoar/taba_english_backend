from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from custom_auth.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authtoken.models import Token

# Create your views here.

class Registration(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def post(self, request, format = None):
		user_serializer = UserSerializer(data=request.data)
		if user_serializer.is_valid():
			user_ins = user_serializer.save()
			result = user_serializer.data
			token, created = Token.objects.get_or_create(user=user_ins)
			result['token'] = token.key
			return Response(result, status=status.HTTP_201_CREATED)
		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)