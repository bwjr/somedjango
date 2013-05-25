from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from writing.models import Paper, Comments

def index(request):
    get_papers = Paper.objects.all().order_by('-time')
    return render(request, 'writing/index.html', {'get_papers': get_papers})

def paper(request, t):
    get_paper = get_object_or_404(Paper, title=t)
    return render(request, 'writing/paper.html', {'get_paper': get_paper})