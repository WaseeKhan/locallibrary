from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre


# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_instances_maintenance = BookInstance.objects.filter(status__exact='m').count()
    num_authors = Author.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_instances_maintenance': num_instances_maintenance,
    }
    return render(request, 'index.html', context=context)


def books(request):
    all_instances = Book.objects.all().count()
    all_books_list = Book.objects.all()
    context ={
        'all_instances': all_instances,
        'all_books_list': all_books_list,
    }
    return render(request, 'books.html', context=context)
