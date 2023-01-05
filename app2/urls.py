from django.urls import path
from app2.views import *
app_name='lord'
urlpatterns=[
    path('GOD/',GOD,name='GOD'),
]