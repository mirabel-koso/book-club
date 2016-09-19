from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from models import Book, Category
from views import ListAllBooks

# Create your tests here.


class CategoryTestCase(TestCase):
    """test for instance of category"""
    # setup
    def setUp(self):
        self.category_object = Category.objects.create(name='test_category')

    # create instance
    def test_is_instance_of_category(self):
        self.assertIsInstance(self.category_object, Category)


class BookTestCase(TestCase):
    """test for instance of book"""
    # setup
    def setUp(self):
        self.category_object = Category.objects.create(name='test_category')
        self.book_object = Book.objects.create(title='test_title', author='test_author', category=self.category_object)

    # create instance
    def test_is_instance_of_book(self):
        self.assertIsInstance(self.book_object, Book)


class HomeViewTestCase(TestCase):
    """test for homeview"""

    # setup
    def setUp(self):
        self.context = {}
        self.client = Client()
        self.category_object = Category.objects.create(name='test_category')
        self.book_object = Book.objects.create(title='test_title', author='test_author', category=self.category_object)

    # home_view_routes_successfully
    def test_routes_to_home_view_successfully(self):
        response = self.client.get(reverse('home_view'))
        self.assertEqual(response.status_code, 200)

    # search_not_in_book_object
    def test_search_not_in_book_object(self):
        result = ListAllBooks.filter_search('dress', self.context)
        search_result = [title for title in result]
        self.assertEqual([], search_result)

    # search_in_book_object
    def test_search_in_book_object(self):
        search_result = ListAllBooks.filter_search('test_title', self.context)
        self.assertEqual(['test_title'], [search_result.first().title])
