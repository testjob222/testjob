from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^user/(?P<username>[\w\-]+)$', views.user_page, name="user_page"),
]