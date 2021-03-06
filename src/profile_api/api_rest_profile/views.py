from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import models
from . import permissions
from . import serializers


class HelloApiView(APIView):

	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		an_apiview = [
			'Lets take a look at a quick example of using REST framework to build a simple ',
			'Lets take a look at aquick example of using REST framework to build a simple ',
			'Lets take a look at aquick example of using REST framework to build a simple',
			'Lets take a look at aquick example of using REST framework to build a simple'
		]
		return Response({'message': 'Hello!', 'api': an_apiview})

	def post(self, request):
		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):

		return Response({'message': 'put'})

	def patch(self, request, pk=None):

		return Response({'message': 'patch'})

	def delete(self, request, pk=None):

		return Response({'message': 'delete'})


class HelloViewSet(viewsets.ViewSet):

	serializer_class = serializers.HelloSerializer

	def list(self, request):
		a_viewset = [
			'Uses actions list, create, retrieve, update, partial_update'
		]
		return Response({"message": "Hello", 'aviset': a_viewset})

	def create(self, request):
		serializer = serializers.HelloSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name').encode('utf-8')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):

		return Response({'HTTP_method': 'GET'})

	def update(self, request, pk=None):

		return Response({'HTTP_method': 'PUT'})

	def partial_update(self, request, pk=None):

		return Response({'HTTP_method': 'PATCH'})

	def destroy(self, request, pk=None):

		return Response({'HTTP_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()

	authentication_classes = (TokenAuthentication, )
	permission_classes = (permissions.UdateOwnProfile, )
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):

	serializer_class = AuthTokenSerializer

	def create(self, request):

		return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
	authentication_classes = (TokenAuthentication,)
	serializer_class = serializers.ProfileFeedItemSerializer
	queryset = models.ProfileFeedItem.objects.all()
	permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

	def perform_create(self, serializer):
		serializer.save(user_profile=self.request.user)





