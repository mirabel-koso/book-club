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

    def test_category_name_exists(self):
        name_field = Category.objects.get(name='test_category')
        self.assertEqual('test_category', name_field.name)

    def test_category_name_does_not_exist(self):
        self.assertRaises(Category.DoesNotExist, Category.objects.get, name__exact='fish')


class BookTestCase(TestCase):
    """test for instance of book"""
    # setup
    def setUp(self):
        self.category_object = Category.objects.create(name='test_category')
        self.book_object = Book.objects.create(title='test_title', author='test_author', category=self.category_object)

    # create instance
    def test_is_instance_of_book(self):
        self.assertIsInstance(self.book_object, Book)

    def test_book_title_exist(self):
        title_field = Book.objects.get(title='test_title')
        self.assertEqual('test_title', title_field.title)

    def test_book_title_does_not_exist(self):
        self.assertRaises(Book.DoesNotExist, Book.objects.get, title__exact='dress')

    def test_book_author(self):
        author_field = Book.objects.get(author='test_author')
        self.assertEqual('test_author', author_field.author)

    def test_book_author_does_not_exist(self):
        self.assertRaises(Book.DoesNotExist, Book.objects.get, author__exact='noauthor')

    def test_category_author(self):
        category_field = Book.objects.get(category__name='test_category')
        self.assertEqual('test_category', category_field.category.name)

    def test_book_category_does_not_exist(self):
        self.assertRaises(Book.DoesNotExist, Book.objects.get, category__name__exact='nocategory')


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
