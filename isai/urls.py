from django.urls import path
from isai.views import *
app_name='call1'
urlpatterns=[
    path('isai/',isai,name='isai')
]