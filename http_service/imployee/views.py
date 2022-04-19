from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Imployee, VacationDate

def index(req):
    imployee = Imployee.objects.all()
    vacation = VacationDate.objects.all()
    body = {'imployee': imployee, 'vacation': vacation, 'title': 'Список сотрудников'}
    return render(req, 'imployee/index.html', body)

class ImployeeView(APIView):
    def get(self, req):
        imployees = Imployee.objects.all()
        return Response({"imployees": imployees})

class VacationView(APIView):
    def get(self, req):
        vacation = VacationDate.objects.all()
        return Response({"vacations": vacation})

