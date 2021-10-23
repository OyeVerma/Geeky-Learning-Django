from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'signals/index.html', {
        'title':'__SIGNALS__'
    })