from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^add_words$', views.add_words),
    url(r'^clear$', views.clear),
    url(r'^$', views.index),
]
