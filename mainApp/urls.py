from django.urls import path
from .views import UpdateDeleteToDo, ListCreateToDo

urlpatterns = [
    path('<int:pk>', UpdateDeleteToDo.as_view()),
    path('', ListCreateToDo.as_view(), name='ListCreateToDo')
]