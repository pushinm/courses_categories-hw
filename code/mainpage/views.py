from django.shortcuts import render
from teachers.models import Teacher
from subjects.models import Subject
from testimonials.models import Testimonial
from icecream import ic
from django.db.models import Q
# Create your views here.

def show_mainpage(request):
    template_ = 'mainpage.html'
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    checked_tests = Testimonial.objects.filter(Q(active=True))
    # ic(teachers.subject)
    context = {
        'teachers': teachers,
        'subjects': subjects,
        'checked_testimonials': checked_tests
    }
    return render(request=request, template_name=template_, context=context)
