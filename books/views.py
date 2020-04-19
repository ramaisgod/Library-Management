from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import csv
from django.db.models import Q
from datetime import datetime


# Create your views here.
def home_page(request):
    return render(request, 'books/index.html', {})


def add_books(request):
    form = BooksForm()
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Books has been added !!!"
            return render(request, 'books/add_books.html', {'form': form, 'message': message})
    return render(request, 'books/add_books.html', {'form': form})


def download_page(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        obj_books = Books.objects.filter(Q(Publish_Date__gte=start_date) & Q(Publish_Date__lte=end_date))
        meta = Books._meta
        field_name = [field.name for field in meta.fields]
        filename = "BooksData_" + str(datetime.now().strftime("%d%m%Y%H%M%S")) + ".csv"
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        writer = csv.writer(response)
        writer.writerow(field_name)
        for obj in obj_books:
            row = writer.writerow([getattr(obj, field) for field in field_name])
        return response
    return render(request, 'books/download_page.html', {})

