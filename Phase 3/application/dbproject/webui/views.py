from shutil import ExecError
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from matplotlib.pyplot import table
from matplotlib.style import context
from django.core.exceptions import FieldError
from django.db.models import Field
from django.forms.models import model_to_dict
from django.apps import apps
import json
from ast import literal_eval

from pytest import Instance

TABLES = [x.__name__ for x in apps.get_models() if not x.__name__.startswith('Auth') and not x.__name__.startswith('Django')]
REQUEST_TABLE_KEY = 'table'
REQUEST_FIELD_KEY = 'column'
REQUEST_VALUE_KEY = 'value'
REQUEST_DELETE_TABLE_KEY = 'delete_table'
REQUEST_DELETE_DATA_KEY = 'delete_data'
BUTTON_SEARCH_KEY = 'search'
BUTTON_DELETE_KEY = 'delete'


def home(request):
    context = {
        'tables': TABLES,
        'header': [],
        'data': [],
    }
    if request.method == 'POST':
        if BUTTON_DELETE_KEY in request.POST:
            delete(request, context)
        elif BUTTON_SEARCH_KEY in request.POST:
            search(request, context)
        else:
            insert(request, context)
    return render(request, 'webui/home2.html', context)


def delete(request, context):
    table_name = request.POST.get(REQUEST_TABLE_KEY, None)
    field_name = request.POST.get(REQUEST_FIELD_KEY, None)
    field_value = request.POST.get(REQUEST_VALUE_KEY, None)
    if table_name:
        model = apps.get_model('webui', table_name)
    if table_name and field_name:
        try:
            model.objects.filter(**{field_name: field_value}).delete()
        except FieldError:
            pass


def insert(request, context):
    table_name = request.POST.get(REQUEST_TABLE_KEY, None)
    if table_name:
        model = apps.get_model('webui', table_name)
        


def search(request, context):
    table_name = request.POST.get(REQUEST_TABLE_KEY, None)
    field_name = request.POST.get(REQUEST_FIELD_KEY, None)
    field_value = request.POST.get(REQUEST_VALUE_KEY, None)
    if table_name:
        model = apps.get_model('webui', table_name)
        context['header'] = [x.name for x in model._meta.get_fields() if isinstance(x, Field)]
    if table_name and field_name:
        try:
            context['data'] = [model_to_dict(x) for x in model.objects.filter(**{field_name: field_value})]
        except FieldError:
            pass
    elif table_name:
        context['data'] = [x.__dict__ for x in model.objects.all()]


def insert(request):
    return render(request, 'webui/insert.html')


def about(request):
    return render(request, 'webui/about.html')
