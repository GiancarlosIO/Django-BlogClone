from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^about/$', views.AboutView.as_view(), name='about'),
]