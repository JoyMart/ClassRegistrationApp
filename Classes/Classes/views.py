from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    languages = ["Python", "C++", "CSS", "HTML", "JavaScript", "SQL"]
    context = {
        'languages': languages
    }
    return render(request, "home.html", context)