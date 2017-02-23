from django.shortcuts import render
from .models import NetworkAnalysis
from django.utils import timezone

def analysis_list(request):
    netans = NetworkAnalysis.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'createnetwork/analysis_list.html', {'netans':netans})
