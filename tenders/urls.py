from django.conf.urls import url

from . import views

app_name = 'tenders'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^procurers/$', views.ProcurersView.as_view(), name='procurers'),
]
