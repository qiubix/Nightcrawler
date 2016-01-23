from hamcrest import *
from django.core.urlresolvers import reverse
from django.test import TestCase


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


class ProcurersViewTests(TestCase):
    def test_procurer_view_with_no_data(self):
        response = self.client.get(reverse('tenders:procurers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No procurers are available.")
        self.assertQuerysetEqual(response.context['all_procurers_list'], [])
