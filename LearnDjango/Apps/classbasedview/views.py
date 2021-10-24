from django.shortcuts import redirect, render
from django.views import View
from .forms import StudentForm

class MyView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'classbasedview/index.html', {
        'title':'__Class Based View__',
        'form':form,
    })

    def post(self, request):
        form_data = StudentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('index-core')


