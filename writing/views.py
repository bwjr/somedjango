from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from writing.models import Paper, Comments, PaperForm

class IndexView(generic.ListView):
    template_name = 'writing/index.html'
    context_object_name = 'get_papers'

    def get_queryset(self):
        return Paper.objects.all().order_by('-time')

@login_required(login_url='/writing/login/')
def paper(request, t):
    get_paper = get_object_or_404(Paper, title=t)
    return render(request, 'writing/paper.html', {'get_paper': get_paper})

@login_required(login_url='/writing/login/')
def add_paper(request):
    if request.method == 'POST':
        form = PaperForm(request.POST, instance = Paper(by_user = request.user))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/writing/')
    else:
        form = PaperForm()

    return render(request, 'writing/addpaper.html', {'form': form})
