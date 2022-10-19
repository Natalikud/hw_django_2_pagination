from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', 'r', encoding = 'utf-8') as file:
        page_number = int(request.GET.get("page",1))
        reader = list(csv.DictReader(file))
        paginator = Paginator(reader,10)
        page = paginator.get_page(page_number)

        context = {
            'bus_stations': reader,
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
