from django.shortcuts import render
from .models import Page
from .forms import PageForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        data = PageForm(request.POST)
        if data.is_valid():
            data.save()
    else:
        form = PageForm()
    return render(request, 'onetoone/index.html', {
        'title':'__One to One__',
        'form':form,
    })