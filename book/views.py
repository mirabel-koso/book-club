from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Q

from models import Book, Category

# Create your views here.


class ListAllBooks(TemplateView):

    template_name = 'index.html'

    @staticmethod
    def filter_search(search_query, context):
        pass