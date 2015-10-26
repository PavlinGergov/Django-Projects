from django.conf.urls import url

from .views import index, get_students, get_emails

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/get-students/(?P<course>[-\w]+)/$', get_students, name="get_students"),
    url(r'^api/get-emails/$', get_emails, name="get_emails"),
]
