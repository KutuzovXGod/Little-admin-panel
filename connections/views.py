from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from connections.models import Agreements, Connections
from connections.forms import EditAgreementForm





def index(request):
    context = {
        'index': Connections.objects.all(),
    }
    return render(request, 'list_agreements.html', context)


class Search(ListView):
    template_name = 'list_agreements.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Connections.objects.filter(
            Q(city__icontains=query) |
            Q(house__icontains=query) |
            Q(street__icontains=query) |
            Q(agreement__username__icontains=query)
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def show_agreement(request, agreement_id):
    agreement_object = Agreements.objects.all().filter(id=agreement_id)
    return render(request, 'agreements.html', context={"agreements": agreement_object})


def update_page(request, pk):
    get_article = Agreements.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAgreementForm(request.POST, instance=get_article)
        if form.is_valid():
            form.save()

    template = 'list_agreements.html'
    context = {
        'get_article': get_article,
        'form': EditAgreementForm(instance=get_article),
        'update': True
    }
    return render(request, template, context)
