from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from writing.models import Paper, Comments

class IndexView(generic.ListView):
    template_name = 'writing/index.html'
    context_object_name = 'get_papers'

    def get_queryset(self):
        return Paper.objects.all().order_by('-time')

def paper(request, t):
    get_paper = get_object_or_404(Paper, title=t)
    return render(request, 'writing/paper.html', {'get_paper': get_paper})
