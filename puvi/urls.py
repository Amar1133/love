from puvi.views import *
from django.urls import path
app_name='call2'
urlpatterns=[
    path('puvi/',puvi,name='puvi'),
]
