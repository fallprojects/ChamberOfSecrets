from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('documents',DocumentView)
router.register('register',AccountRegisterView)


urlpatterns = [
    path('',include(router.urls)),
    path('login/',AccountLoginView.as_view(),name='login'),
    path('document_filter/', DocumentViewFilter.as_view(), name='document_filter')
]