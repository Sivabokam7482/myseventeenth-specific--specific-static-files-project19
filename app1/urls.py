from django.urls import path
from app1.views import *
app_name='cva'
urlpatterns=[
    path('siva/',siva,name='siva'),
]