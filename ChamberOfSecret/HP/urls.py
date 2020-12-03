from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('documents',DocumentsView)
router.register('register',AccountRegisterView)


urlpatterns = [
    path('',include(router.urls)),
    path('auth',AccountLoginView.as_view(),name='auth')
]