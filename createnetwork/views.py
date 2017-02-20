from django.shortcuts import render

def analysis_list(request):
    return render(request, 'createnetwork/analysis_list.html', {})
