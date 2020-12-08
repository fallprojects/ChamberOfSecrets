
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group

# def unauth_user(view_funk):
#         def wrapped(request,*args,**kwargs):
#             if request.user.is_authenticated:
#                 return redirect('HP')
#             else:
#                 return view_funk(request,*args,**kwargs)
#         return wrapped
