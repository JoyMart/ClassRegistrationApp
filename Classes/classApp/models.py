from django.http import HttpResponse
from django.db import models
from django.shortcuts import render


class djangoClasses(models.Model):
    Title = models.CharField(max_length=30, null=False)
    CourseNumber = models.IntegerField()
    InstructorName = models.CharField(max_length=50, null=False)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title


beginner_object = djangoClasses(
    1,
    'Django101',
    101,
    "George MacAfee",
    60.00)
beginner_object.save()
beginner_object.__str__()

intermediate_object = djangoClasses(
    2,
    'Django201',
    201,
    "Jill Roller",
    60.00
)
intermediate_object.save()
intermediate_object.__str__()

expert_object = djangoClasses(
    3,
    'Django301',
    301,
    "Max Ludvig",
    60.00
)
expert_object.save()
expert_object.__str__()