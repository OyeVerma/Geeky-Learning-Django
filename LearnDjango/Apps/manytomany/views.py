from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'manytomany/index.html', {
        'title':'__Many to Many__'
    })