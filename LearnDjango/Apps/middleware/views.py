from django.shortcuts import render

# Create your views here.
def index(request):
    print('I am View')
    return render(request, 'middleware/index.html', {
        'title':'__MIDDLEWARE__'
    })