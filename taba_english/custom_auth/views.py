from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from custom_auth.serializers import UserAuthSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class Registration(APIView):

	def post(self, request, format=None):
		user_serializer = UserAuthSerializer(data=request.data)
		if user_serializer.is_valid():
			email = user_serializer.data['email']
			username = email
			password = user_serializer.data['password']
			if len(User.objects.filter(username=username)):
				return Response({'desc': 'username already exist'}, status=status.HTTP_400_BAD_REQUEST)
			user_ins = User.objects.create_user(username=username, password=password, email=email)
			token, created = Token.objects.get_or_create(user=user_ins)
			resp = {'token': token.key, 'username': username}
			return Response(resp, status=status.HTTP_201_CREATED)
		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
	def post(self, request, format=None):
		user_serializer = UserAuthSerializer(data=request.data)
		if user_serializer.is_valid():
			email = user_serializer.data['email']
			username = email
			password = user_serializer.data['password']
			user_ins = authenticate(username=username, password=password)
			if user_ins:
				login(request, user_ins)
				token, created = Token.objects.get_or_create(user=user_ins)
				resp = {'token': token.key, 'username': username}
				return Response(resp, status=status.HTTP_200_OK)
			else:
				return Response({'desc': 'wrong information'}, status=status.HTTP_401_UNAUTHORIZED)
		return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
	def post(self, request, format=None):
		try:
			logout(request)
			return Response({'successfull': True, 'desc': 'logout successfully'}, status=status.HTTP_200_OK)
		except Exception as e:
			return Response({'successfull': False, 'desc': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class IsAuthenticated(APIView):
	def get(self, request):
		if request.user.is_authenticated:
			return Response({'successfull': True, 'authenticated': True}, status=status.HTTP_200_OK)
		else:
			return Response({'successfull': True, 'authenticated': False}, status=status.HTTP_401_UNAUTHORIZED)
