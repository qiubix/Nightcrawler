from django.conf.urls import url

from . import views

app_name = 'tenders'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^displayProcurers$', views.displayProcurers, name='displayProcurers'),
    url(r'^procurers/$', views.ProcurersView.as_view(), name='procurers'),
    url(r'^contractors/$', views.ContractorsView.as_view(), name='contractors'),
    url(r'^import/$', views.importView, name='import'),
]
