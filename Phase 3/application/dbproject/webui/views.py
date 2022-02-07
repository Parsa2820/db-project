from shutil import ExecError
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.urls import reverse
from matplotlib.pyplot import table
from matplotlib.style import context
from django.core.exceptions import FieldError
from django.db.models import Field
from django.forms.models import model_to_dict
from django.apps import apps
from .forms import *

from pytest import Instance

TABLES = [x.__name__ for x in apps.get_models() if not x.__name__.startswith('Auth') and not x.__name__.startswith('Django')][:-6]
REQUEST_TABLE_KEY = 'table'
REQUEST_FIELD_KEY = 'column'
REQUEST_VALUE_KEY = 'value'
REQUEST_DELETE_TABLE_KEY = 'delete_table'
REQUEST_DELETE_DATA_KEY = 'delete_data'
BUTTON_SEARCH_KEY = 'search'
BUTTON_DELETE_KEY = 'delete'
BUTTON_INSERT_KEY = 'insert'
BUTTON_GET_FORM_KEY = 'get_form'
BUTTON_CANCEL_KEY = 'cancel'


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
        elif BUTTON_INSERT_KEY in request.POST:
            return redirect('webui-insert')
    print(len(context['data']))
    print(context['header'])
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


def init_insert(request):
    table_name = request.POST.get(REQUEST_TABLE_KEY, None)
    if table_name:
        model = apps.get_model('webui', table_name)
        form_name = model.__name__ + 'Form'
        form_class = globals()[form_name]
        form = form_class()
        return render(request, 'webui/insert2.html', {'form': form, 'tables': [table_name]})
    return HttpResponse('internal error: table name not found')



def insert(request):
    form = None
    if request.method == 'POST':
        if BUTTON_GET_FORM_KEY in request.POST:
            return init_insert(request)
        elif BUTTON_INSERT_KEY in request.POST:
            table_name = request.POST.get(REQUEST_TABLE_KEY, None)
            model = apps.get_model('webui', table_name)
            form_name = model.__name__ + 'Form'
            form_class = globals()[form_name]
            form = form_class(request.POST)
            if form.is_valid():
                form.save()
            else:
                pks = [x.name for x in model._meta.get_fields() if isinstance(x, Field) and x.primary_key]
                row = {}
                for pk in pks:
                    row[pk] = request.POST.get(pk, None)
                try:
                    obj = model.objects.get(**row)
                    form = form_class(request.POST, instance=obj)
                    form.save()
                except:
                    # form not loaded yet
                    return render(request, 'webui/insert2.html', {'tables': TABLES})
            return redirect("webui-home")
        elif BUTTON_CANCEL_KEY in request.POST:
            return redirect("webui-home")
    return render(request, 'webui/insert2.html', {'tables': TABLES})



def search(request, context):
    table_name = request.POST.get(REQUEST_TABLE_KEY, None)
    field_name = request.POST.get(REQUEST_FIELD_KEY, None)
    field_value = request.POST.get(REQUEST_VALUE_KEY, None)
    print(f'{table_name=} {field_name=} {field_value=}')
    if table_name:
        model = apps.get_model('webui', table_name)
        context['header'] = [x.name for x in model._meta.get_fields() if isinstance(x, Field)]
    if table_name and field_name:
        try:
            row_dict = [x.__dict__ for x in model.objects.filter(**{field_name: field_value})]
            for row in row_dict:
                expanded_dict = {}
                for key, value in row.items():
                    if key.endswith('_id'):
                        expanded_dict[key[:-3]] = value
            row.update(expanded_dict)
            context['data'] = row_dict
        except FieldError:
            pass
    elif table_name:
        row_dict = [x.__dict__ for x in model.objects.all()]
        for row in row_dict:
            expanded_dict = {}
            for key, value in row.items():
                if key.endswith('_id'):
                    expanded_dict[key[:-3]] = value
            row.update(expanded_dict)
        context['data'] = row_dict


def about(request):
    return render(request, 'webui/about.html')
