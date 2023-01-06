from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from connections.models import Agreements, Connections


def index(request):
    context = {
        'index': Agreements.objects.all(),
        'HM': Connections.objects.all(),
    }
    return render(request, 'list_agreements.html', context)


class SearchByConnections(ListView):
    template_name = 'list_agreements.html'
    context_object_name = 'Connections'

    def get_queryset(self):
        return Connections.objects.filter(city__icontains=self.request.GET.get('q'))  #поиск не работает

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class Search(ListView):
    template_name = 'list_agreements.html'
    context_object_name = 'Agreements'

    def get_queryset(self):
        return Agreements.objects.filter(username__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


