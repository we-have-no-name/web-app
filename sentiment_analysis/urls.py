from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'sentiment_analysis'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^data/', views.DataViewSet.as_view(), name='about'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
