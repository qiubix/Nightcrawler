import googlemaps
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import generic

from Nightcrawler.settings import GOOGLE_API_SECRET_KEY
from tenders.CompanyLocator import CompanyLocator
from tenders.DataReader import DataReader
from .models import Procurer, Tender, Contractor


class IndexView(generic.ListView):
    template_name = 'tenders/index.html'
    context_object_name = 'procurers'

    def get_queryset(self):
        return Procurer.objects.all()


class ProcurersView(generic.ListView):
    template_name = 'tenders/procurers.html'
    context_object_name = 'all_procurers_list'

    def get_queryset(self):
        return Procurer.objects.all()


class ContractorsView(generic.ListView):
    template_name = 'tenders/contractors.html'
    context_object_name = 'all_contractors_list'

    def get_queryset(self):
        return Contractor.objects.all()


def importView(request):
    reader = DataReader()
    reader.load('data/2007-08-01-mazowieckie.xml')
    procurers = reader.getProcurers()
    print('procurers size: ', len(procurers))
    contractors = reader.getContractors()
    for procurer in procurers:
        Procurer.objects.create(company_name=procurer.company_name, city=procurer.city, address=procurer.full_address)

    for contractor in contractors:
        Contractor.objects.create(company_name=contractor.company_name, city=contractor.city,
                                  address=contractor.full_address)

    return HttpResponse('<h2>Data imported!</h2>')


def displayProcurers(request):
    procurer = get_object_or_404(Procurer, pk=2)
    if procurer.latitude is None or procurer.longitude is None:
        gmapsClient = googlemaps.Client(key=GOOGLE_API_SECRET_KEY)
        locator = CompanyLocator(gmapsClient)
        location = locator.getLocation(procurer.address)
        procurer.latitude = location.get('lat')
        procurer.longitude = location.get('lng')
        procurer.save()

    return HttpResponseRedirect(reverse('tenders:index'))

