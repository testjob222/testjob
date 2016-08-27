from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^user/(?P<vkuser>[\w\-]+)$', views.user_page, name="user_page"),
]
]