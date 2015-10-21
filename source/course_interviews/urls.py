from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/get_students/(?P<course>[-\w]+)/$', get_students, name="get_students"),
]
