from django.shortcuts import render
from .models import djangoClasses


def admin_console(request):
    classes = djangoClasses.objects.all()
    return render(request, 'ClassApp/django_classes.html', {'classes': classes})


