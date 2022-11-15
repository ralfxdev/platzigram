"""Platzigram Views module."""

#Django
import numbers
from urllib import response
from django.http import HttpResponse
from django.http import JsonResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

def sort(request):
    """HttpResponse."""
    #numbers = request.GET['numbers']
    #return HttpResponse(str(numbers))

    """HttpResponse with Json."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(str(json.dumps(data)), content_type='application/json')

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram'.format(name)
    return HttpResponse(message)
