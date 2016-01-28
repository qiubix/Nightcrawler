from hamcrest import *
from django.core.urlresolvers import reverse
from django.test import TestCase

from tenders.TestTemplates import getSampleText
from .models import Procurer, Contractor
from .DataReader import DataReader, ProcurerData


# Create your tests here.
class ModelTests(TestCase):
    def test_should_test_nothing_yet(self):
        self.assertEqual(1, 1)


class IndexViewTests(TestCase):
    def test_index_view_with_no_data(self):
        response = self.client.get(reverse('tenders:index'))
        assert_that(response.status_code, equal_to(200))
        self.assertContains(response,
                            "This site displays map of contractors and procurers connected by executed contracts.")


def createProcurer(companyName, city, address):
    return Procurer.objects.create(company_name=companyName, city=city, address=address)


class ProcurersViewTests(TestCase):
    def test_procurer_view_with_no_data(self):
        response = self.client.get(reverse('tenders:procurers'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No procurers are available.")
        self.assertQuerysetEqual(response.context['all_procurers_list'], [])

    def test_should_display_table_when_procurers_exist(self):
        createProcurer('Company name', 'Some City', 'Full address')

        response = self.client.get(reverse('tenders:procurers'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<table>')
        self.assertContains(response, '<th>ID</th>')
        self.assertContains(response, '<th>Company name</th>')
        self.assertContains(response, '<th>City</th>')
        self.assertContains(response, '<th>Full address</th>')

    def test_should_display_one_procurer_in_table(self):
        createProcurer('Company name', 'Some City', 'Full address')

        response = self.client.get(reverse('tenders:procurers'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['all_procurers_list'], ['<Procurer: Company name>'])
        self.assertContains(response, '<td>Company name</td>')
        self.assertContains(response, '<td>Some City</td>')
        self.assertContains(response, '<td>Full address</td>')

    def test_should_display_multiple_procurers(self):
        createProcurer('First', 'City 1', 'Street 1')
        createProcurer('Second', 'City 2', 'Street 2')
        createProcurer('Third', 'City 3', 'Street 3')

        response = self.client.get(reverse('tenders:procurers'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['all_procurers_list'],
                                 ['<Procurer: First>', '<Procurer: Second>', '<Procurer: Third>'], ordered=False)
        self.assertContains(response, '<td>First</td>')
        self.assertContains(response, '<td>City 2</td>')
        self.assertContains(response, '<td>Street 3</td>')


def createContractor(companyName, city, address):
    return Contractor.objects.create(company_name=companyName, city=city, address=address)


class ContractorsViewTests(TestCase):
    def test_procurer_view_with_no_data(self):
        response = self.client.get(reverse('tenders:contractors'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No contractors are available.")
        self.assertQuerysetEqual(response.context['all_contractors_list'], [])

    def test_should_display_table_when_contractors_exist(self):
        createContractor('Company name', 'Some City', 'Full address')

        response = self.client.get(reverse('tenders:contractors'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<table>')
        self.assertContains(response, '<th>ID</th>')
        self.assertContains(response, '<th>Company name</th>')
        self.assertContains(response, '<th>City</th>')
        self.assertContains(response, '<th>Full address</th>')

    def test_should_display_one_contractor_in_table(self):
        createContractor('Company name', 'Some City', 'Full address')

        response = self.client.get(reverse('tenders:contractors'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['all_contractors_list'], ['<Contractor: Company name>'])
        self.assertContains(response, '<td>Company name</td>')
        self.assertContains(response, '<td>Some City</td>')
        self.assertContains(response, '<td>Full address</td>')

    def test_should_display_multiple_contractors(self):
        createContractor('First', 'City 1', 'Street 1')
        createContractor('Second', 'City 2', 'Street 2')
        createContractor('Third', 'City 3', 'Street 3')

        response = self.client.get(reverse('tenders:contractors'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['all_contractors_list'],
                                 ['<Contractor: First>', '<Contractor: Second>', '<Contractor: Third>'], ordered=False)
        self.assertContains(response, '<td>First</td>')
        self.assertContains(response, '<td>City 2</td>')
        self.assertContains(response, '<td>Street 3</td>')


class ProcurerDataTests(TestCase):
    def test_should_have_empty_company_name_on_init(self):
        procurerData = ProcurerData()

        assert_that(procurerData.company_name, equal_to(''))

    def test_should_have_empty_city_on_init(self):
        procurerData = ProcurerData()

        assert_that(procurerData.city, equal_to(''))


class DataReaderTests(TestCase):
    def test_should_get_only_one_contractor(self):
        reader = DataReader()

        reader.load('data/test/one_tender.xml')

        contractors = reader.getContractors()
        assert_that(len(contractors), equal_to(1))

    def test_should_get_two_procurers(self):
        reader = DataReader()

        reader.load('data/test/one_tender.xml')

        procurers = reader.getProcurers()
        assert_that(len(procurers), equal_to(2))

    def test_should_get_procurers_with_correct_name(self):
        reader = DataReader()

        reader.load('data/test/one_tender.xml')

        procurers = reader.getProcurers()
        assert_that(len(procurers), greater_than(0))
        firstProcurer = procurers[0]
        assert_that(firstProcurer, is_not(None))
        assert_that(firstProcurer.company_name, equal_to('Oddział Specjalny Żandarmerii Wojskowej'))
        secondProcurer = procurers[1]
        assert_that(secondProcurer, is_not(None))
        assert_that(secondProcurer.company_name, equal_to('Centrum Onkologii Instytut im. Marii Skłodowskiej-Curie'))

    def test_should_get_procurers_with_correct_city(self):
        reader = DataReader()

        reader.load('data/test/one_tender.xml')

        procurers = reader.getProcurers()
        assert_that(len(procurers), greater_than(0))
        firstProcurer = procurers[0]
        assert_that(firstProcurer, is_not(None))
        assert_that(firstProcurer.city, equal_to('Mińsk Mazowiecki'))
        secondProcurer = procurers[1]
        assert_that(secondProcurer, is_not(None))
        assert_that(secondProcurer.city, equal_to('Warszawa'))

    def test_should_extract_procurers_address_from_text(self):
        reader = DataReader()

        address = reader.extractProcurersAddress(getSampleText())

        assert_that(address, equal_to('ul. Warszawska, 05-300 Mińsk Mazowiecki'))

    def test_should_get_procurer_full_address(self):
        reader = DataReader()

        reader.load('data/test/one_tender.xml')

        procurers = reader.getProcurers()
        assert_that(len(procurers), greater_than(0))
        firstProcurer = procurers[0]
        assert_that(firstProcurer, is_not(None))
        assert_that(firstProcurer.full_address, equal_to('ul. Warszawska, 05-300 Mińsk Mazowiecki'))
        secondProcurer = procurers[1]
        assert_that(secondProcurer, is_not(None))
        assert_that(secondProcurer.full_address, equal_to('ul. W.K. Roentgena 5, 02-781 Warszawa'))

    def test_should_extract_contractor_name_from_text(self):
        reader = DataReader()

        name = reader.extractContractorName(getSampleText())

        assert_that(name, equal_to('HOLSTERS HPE Polska Grzegorz Szymański'))

    def test_should_get_contractors_with_correct_name(self):
        reader = DataReader()

        reader.load('data/test/one_tender.xml')

        contractors = reader.getContractors()
        assert_that(len(contractors), greater_than(0))
        firstContractor = contractors[0]
        assert_that(firstContractor, is_not(None))
        assert_that(firstContractor.company_name, equal_to(''))
