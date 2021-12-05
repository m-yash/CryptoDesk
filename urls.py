from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url('home/',views.index),
    path('feed/<id>',views.feeds,name='feed_page'),
]
