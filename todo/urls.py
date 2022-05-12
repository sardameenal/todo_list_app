from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addtodo, name='add'),
    path('complete/<todo_id>', views.completetodo, name='complete'),
    path('deletecomplete', views.deletecompleted, name='deletecomplete'),
    path('deleteall', views.deleteall, name='deleteall')
]