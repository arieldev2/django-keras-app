from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Classification


class ClassificationListview(ListView):
    model = Classification
    template_name= 'cnn/classification_list.html'
    context_object_name = 'items'


class ClassificationCreateView(CreateView):
    model = Classification
    fields = ['img']


class ClassificationUpdateView(UpdateView):
    model = Classification
    fields = ['img']


class ClassificationDeleteView(DeleteView):
    model = Classification
    success_url = '/'
