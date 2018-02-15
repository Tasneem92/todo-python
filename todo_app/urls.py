from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^new/$', views.new_post, name='new_post'),
    url(r'^form/$', views.post_form, name='post_form'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
