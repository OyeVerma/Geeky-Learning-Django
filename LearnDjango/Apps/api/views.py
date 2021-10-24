from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Teacher
from .forms import TeacherForm
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def data(request, pk):
    data = Teacher.objects.get(pk=pk)

    # serializing data
    serializer  = TeacherSerializer(data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

class MyIndex(View):
    def get(self, request):
        print(1)
        return render(request, 'api/index.html', {
            'title':'__Api__',
            'form':TeacherForm
        })

    def post(self, request):
        form_data = TeacherForm(request.POST)
        if form_data.is_valid():
            form_data.save()
