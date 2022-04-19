
from django.urls import path, include
from .views import index, ImployeeView, VacationView
from .models import VacationDate, Imployee


urlpatterns = [
    path('', index),
    path('api/imployee', ImployeeView.as_view()),
    path('api/vacation', VacationView.as_view())
]