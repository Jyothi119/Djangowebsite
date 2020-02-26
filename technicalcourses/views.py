from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import allcourses


def courses(request):
    ac=allcourses.objects.all()
    template=loader.get_template('technicalcourses/courses.html')
    context={
        'ac':ac
    }
    return HttpResponse(template.render(context, request))

def details(request, course_id):
    try:
        course=allcourses.objects.get(pk=course_id)
    except allcourses.DoesNotExist:
        raise Http404("course not available")
    return render(request, 'technicalcourses/detail.html', {'course':course})
# Create your views here.
