from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class ListAllBooks(TemplateView):

    @staticmethod
    def filter_search(search_query, context):
        pass