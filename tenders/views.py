from django.http import HttpResponse
from django.views import generic
from .models import Procurer, Tender


class IndexView(generic.ListView):
    template_name = 'tenders/index.html'
    context_object_name = 'tenders'

    def get_queryset(self):
        return Tender.objects.all()


class ProcurersView(generic.ListView):
    template_name = 'tenders/procurers.html'
    context_object_name = 'all_procurers_list'

    def get_queryset(self):
        return Procurer.objects.all()
