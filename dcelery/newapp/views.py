from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sharedtask

def test_task(request):
    result = sharedtask.delay({'name': 'KP'})

    if result.ready():
        return HttpResponse('Task done')
    else:
        return HttpResponse('working on it...')