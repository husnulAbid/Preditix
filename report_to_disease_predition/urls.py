from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include

from report_to_disease_predition.views import *

urlpatterns = [

    url(r'^predict$', Predict.as_view(), name='predict'),
]
