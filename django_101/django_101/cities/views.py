from django.http import HttpResponse
from django.shortcuts import render, redirect

from django_101.cities.models import Person


def index(req):
    context = {
        'name': 'Alex',
        'people': Person.objects.all(),
    }

    return render(req, 'index.html', context)


def create_person(req):
    Person(
        name='Pesho',
        age=11,
        home_town='Sofia',
    ).save()

    return redirect('/cities')


def test_index(req):
    return HttpResponse(
        '{"name": "Alex"}',
        content_type='application/json')


def list_phones(req):
    context = {'phones': [
        {
            'name': 'Galaxy S20',
            'quantity': 3,
        },
        {
            'name': 'Xiaomi Readmi T9',
            'quantity': 4
        },
        {
            'name': 'iPhone 12',
            'quantity': 0
        },
    ], 'message': 'Phones List'}

    return render(req, 'cities/phones.html', context)
