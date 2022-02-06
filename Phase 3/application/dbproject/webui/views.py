from shutil import ExecError
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from matplotlib.pyplot import table
from matplotlib.style import context
from django.core.exceptions import FieldError
from django.db.models import Field
from django.apps import apps


TABLES = [x.__name__ for x in apps.get_models() if not x.__name__.startswith(
    'Auth') and not x.__name__.startswith('Django')]
REQUEST_TABLE_KEY = 'table'
REQUEST_FIELD_KEY = 'column'
REQUEST_VALUE_KEY = 'value'


def home(request):
    context = {
        'tables': TABLES,
        'header': [],
        'data': []
    }
    if request.method == 'POST':
        table_name = request.POST.get(REQUEST_TABLE_KEY, None)
        field_name = request.POST.get(REQUEST_FIELD_KEY, None)
        field_value = request.POST.get(REQUEST_VALUE_KEY, None) 
        if table_name:
            model = apps.get_model('webui', table_name)
            context['header'] = [x.name for x in model._meta.get_fields() if isinstance(x, Field)]
        if table_name and field_name and field_value:
            try:
                context['data'] = [x.__dict__ for x in model.objects.filter(**{field_name: field_value})]
            except FieldError:
                pass
        elif table_name:
            context['data'] = [x.__dict__ for x in model.objects.all()]
    return render(request, 'webui/home.html', context)


def about(request):
    return render(request, 'webui/about.html')
