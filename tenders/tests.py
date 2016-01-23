from hamcrest import *
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Procurer


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
