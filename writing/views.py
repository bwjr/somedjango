from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from writing.models import Paper, Comments, PaperForm

class IndexView(generic.ListView):
    template_name = 'writing/index.html'
    context_object_name = 'get_papers'

    def get_queryset(self):
        return Paper.objects.all().order_by('-time')

def paper(request, t):
    get_paper = get_object_or_404(Paper, title=t)
    return render(request, 'writing/paper.html', {'get_paper': get_paper})

def add_paper(request):
    if request.method == 'POST':
        # Temporary before I get login set up
        if request.user.is_authenticated():
            form = PaperForm(request.POST, instance = Paper(by_user = request.user))
        else:
            form = PaperForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/writing/')
    else:
        form = PaperForm()

    return render(request, 'writing/addpaper.html', {'form': form})
