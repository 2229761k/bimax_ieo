from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^toka/$', views.toka, name='toka'),

    url(r'^gpa/$', views.gpa, name='gpa'),

 ]
