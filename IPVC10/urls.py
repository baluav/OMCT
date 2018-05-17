from django.urls import path
from . import views
from .views import (UserHomeView, AddPatashalaView, ListPatashalasView,
        DetailPatashalaView, UpdatePatashalaView, AddStudentView, ListStudentsView,
        DetailStudentView, UpdateStudentView)

app_name = 'IPVC10'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('login/', views.IndexView.as_view()),
    path('user_login/', views.user_login, name='user_login'),
    path('user_home/', UserHomeView.as_view(), name='user_home'),
    path('patashala-add/', AddPatashalaView.as_view(), name='patashala-add'),
    path('patashalas/', ListPatashalasView.as_view(), name='patashalas'),
    path('patashalas/<int:pk>/', DetailPatashalaView.as_view(), name='patashala_detail'),
    path('patashala-update/<int:pk>/', UpdatePatashalaView.as_view(), name='patashala-update'),
    path('student-add/', AddStudentView.as_view(), name='student-add'),
    path('students/', ListStudentsView.as_view(), name='students'),
    path('students/<int:pk>/', DetailStudentView.as_view(), name='student-detail'),
    path('student-update/<int:pk>/', UpdateStudentView.as_view(), name='student-update'),
]
