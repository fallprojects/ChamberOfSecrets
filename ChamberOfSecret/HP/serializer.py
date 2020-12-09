from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *
from django.contrib.auth.models import User

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name','date_created','mark','text']


class AccountRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name','last_name','phone','role']

class UserSerializer(serializers.ModelSerializer):
    account = AccountRegisterSerializer()

    class Meta:
        model = User
        fields = ['username','password','account',]

    def create(self, validated_data):
        password = self.validated_data.get('password')
        profile_data = validated_data.pop('account')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Account.objects.create(user=user, **profile_data)
        return user
