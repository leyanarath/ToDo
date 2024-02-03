from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<int:todoid>',views.delete,name="delete"),
    path('update/<int:todoid>', views.update, name="update"),
    path('classlist/', views.Todolist.as_view(), name="classlist"),
    path('classdetail/<int:pk>', views.Tododetail.as_view(), name="Tododetail"),
    path('classupdate/<int:pk>', views.Todoupdate.as_view(), name="Todoupdate"),
    path('classdelete/<int:pk>', views.Tododelete.as_view(), name="Tododelete"),
]