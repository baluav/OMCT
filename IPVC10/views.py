from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.views.generic import (View, TemplateView,
    CreateView, ListView, DetailView, UpdateView)
from . import models

import logging

from .models import Patashala, Student, Register

# Get an instance of a logger
logger = logging.getLogger('IPVC10')

# Create your views here.
def index(request):
    num_patashalas =  Patashala.objects.all().count()
    num_students = Student.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_patashalas':num_patashalas, 'num_students':num_students, 'num_visits':num_visits},
    )

class IndexView(TemplateView):
    template_name = 'index.html'

class UserHomeView(TemplateView):
    template_name = 'IPVC10/home.html'

def user_login(request):
    logger.info('Entering user_login...')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                logged_in = True
                logger.debug("User Account active and Login Successful!")
                return HttpResponseRedirect(reverse('IPVC10:user_home'))
            else:
                HttpResponse("Account not active")
        else:
            logger.debug('Someone tried to login and failed. ')
            logger.debug("Username: {%s} and Password: {%s} were provided.",username, password)
            messages.error(request, "Incorrect credentials. Please try again.")
            logger.info("Exiting user_login...")
            #return HttpResponse("Invalid login details supplied")
            return render(request,'login.html',{})
    else:
        logger.info("Exiting user_login...")
        return render(request,'login.html',{})

@login_required
def user_logout(request):
    logger.info('Entering user_logout...')
    logout(request)
    logged_in = False
    logger.info('Exiting user_logout...')
    return HttpResponseRedirect(reverse('index'))

class AddPatashalaView(CreateView):
    logger.info('Entering AddPatashalaView...')
    logger.info('Add a new Patashala')
    fields = ('name', 'address', 'city', 'state',
        'pincode','phone1', 'phone2', 'number_of_students')
    model = models.Patashala
    logger.info('Exiting AddPatashalaView...')

class ListPatashalasView(ListView):
    logger.info('Entering ListPatashalasView...')
    logger.info('Listing of Patashalas')
    context_object_name = "patashalas"
    model = models.Patashala
    queryset = models.Patashala.objects.all()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['patashalas'] = models.Patashala.objects.all()
        return context

    logger.info('Exiting ListPatashalasView...')

class DetailPatashalaView(DetailView):
    logger.info('Entering DetailPatashalaView...')
    logger.info('Detailed view of selected Patashala')
    context_object_name = "patashala_detail"
    model = models.Patashala
    template_name = "IPVC10/patashala-detail.html"
    logger.info('Exiting DetailPatashalaView...')

class UpdatePatashalaView(UpdateView):
    logger.info('Entering UpdatePatashalaView...')
    logger.info('Updation of Patashala details')
    fields = ('name', 'address', 'city', 'state',
        'pincode','phone1', 'phone2', 'number_of_students')
    model = models.Patashala
    logger.info('Exiting UpdatePatashalaView...')

class AddStudentView(CreateView):
    logger.info('Entering AddStudentView...')
    logger.info('Add a new Student')
    fields = ('name', 'parent_name', 'dob','picture','patashala' )
    model = models.Student
    logger.info('Exiting AddStudentView...')

class ListStudentsView(ListView):
    logger.info('Entering ListStudentsView...')
    logger.info('Listing of Students')
    context_object_name = "students"
    model = models.Student
    paginate_by = 5
    queryset = models.Student.objects.all()
    logger.info('Exiting ListStudentsView...')

class DetailStudentView(DetailView):
    logger.info('Entering DetailStudentView...')
    logger.info('Detailed view of selected Student')
    context_object_name = 'student-detail'
    model = models.Student
    template_name = "IPVC10/student-detail.html"
    logger.info('Exiting DetailStudentView...')

class UpdateStudentView(UpdateView):
    logger.info('Entering UpdateStudentView...')
    logger.info('Updation of Student detail')
    fields = ('event_name', 'event_date', 'event_start_time', 'event_end_time')
    model = models.Student
    logger.info('Exiting UpdateStudentView...')
