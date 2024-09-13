from django.db.models import Avg
from django.shortcuts import render
from django.views.generic import ListView, View

from courses.models import Course


# Create your views here.


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course.html'
    context_object_name = 'courses'
