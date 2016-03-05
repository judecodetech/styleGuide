from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.style_guide_list),
]
