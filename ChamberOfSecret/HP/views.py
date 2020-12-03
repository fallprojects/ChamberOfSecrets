from django.shortcuts import render
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializer import *
from rest_framework import status,viewsets,filters,views,generics


class DocumentsView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class AccountRegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AccountLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                            context={'request':request})
        if not serializer.is_valid():
            return Response({'User not found'})
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key
        })



