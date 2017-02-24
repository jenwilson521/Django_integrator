from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import FormView
from .models import NetworkAnalysis
from .forms import MakeNetworkCommand

def analysis_list(request):
    netans = NetworkAnalysis.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'createnetwork/analysis_list.html', {'netans':netans})

class NetworkCommandPage(FormView):
    template_name = 'createnetwork/network_command.html'
    success_url = '/awesome/'
    form_class = MakeNetworkCommand

    def form_valid(self,form):
        return HttpResponse("Sweeeeeet.")
