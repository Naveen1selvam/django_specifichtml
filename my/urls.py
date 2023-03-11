from my.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('sample/',sample,name='sample'),
]