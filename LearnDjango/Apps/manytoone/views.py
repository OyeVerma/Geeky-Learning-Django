from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        data = PostForm(request.POST)
        if data.is_valid():
            data.save()
    else:
        form = PostForm()
    return render(request, 'manytoone/index.html', {
        'title':'__Many to One__',
        'form':form,
    })