from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'filters/index.html', {
        'title':'__FILTERS__',
        'dic':{'name':'Abhishek', 'class':'XII', 'section':'B', 'school':'Sarvodaya Co-ed Vidyalaya No.2'}
    })