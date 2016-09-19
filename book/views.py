from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Q

from models import Book

# Create your views here.


class ListAllBooks(TemplateView):

    template_name = 'index.html'

    def get(self, request):
        context = {}
        search_query = request.GET.get('book_name', '')
        context['books'] = self.filter_search(search_query, context)
        return render(request, self.template_name, context)

    @staticmethod
    def filter_search(search_query, context):
        filter_query = Q(title__icontains=search_query) | Q(category__name__icontains=search_query)
        if search_query:
            context['books'] = Book.objects.filter(filter_query)
        else:
            context['books'] = Book.objects.all()
        return context['books']
