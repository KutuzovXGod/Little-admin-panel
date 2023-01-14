from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from connections.models import Agreements, Connections
from connections.forms import EditAgreementForm, EditConnectionsForm


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


def edit_page(request, pk):
    agreement = Agreements.objects.get(pk=pk)
    connections = Connections.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAgreementForm(request.POST, instance=agreement)
        form1 = EditConnectionsForm(request.POST, instance=connections)
        if form.is_valid() and form1.is_valid():
            form.save() and form1.save()

    template = 'list_agreements.html'
    context = {
        'agreement': agreement,
        'connections': connections,
        'form': EditAgreementForm(instance=agreement),
        'form1': EditConnectionsForm(instance=connections),
        'update': True
    }
    return render(request, template, context)


# def update_page1(request, pk):
#     get_article1 = Connections.objects.get(pk=pk)
#     if request.method == 'POST':
#         form1 = EditConnectionsForm(request.POST, instance=get_article1)
#         if form1.is_valid():
#             form1.save()
#
#     template = 'list_agreements.html'
#     context = {
#         'get_article1': get_article1,
#         'form1': EditConnectionsForm(instance=get_article1),
#         'update': True
#     }
#     return render(request, template, context)

# def update_page(request):
#     if request.method == 'POST':
#         thread_form = EditAgreementForm(request.POST)
#         post_form = EditConnectionsForm(request.POST)
#
#         if thread_form.is_valid() and post_form.is_valid():
#             thread = thread_form.save()
#             post = post_form.save(False)
#
#             post.thread=thread
#             post.save()
#
#             return redirect(reverse)
#
#     else:
#         thread_form = EditAgreementForm()
#         post_form = EditConnectionsForm()
#
#     args = {}
#     args.update(csrf(request))
#     args['thread_form'] = thread_form
#     args['post_form'] = post_form
#
#     return render(request, 'list_agreements.html', args)



