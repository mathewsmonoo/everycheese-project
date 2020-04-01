from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .models import Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country_of_origin']

class CheeseListView(ListView):
    model = Cheese