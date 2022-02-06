from shutil import ExecError
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from matplotlib.style import context
from django.db.models import Field
from django.apps import apps


TABLES = [x.__name__ for x in apps.get_models() if not x.__name__.startswith('Auth') and not x.__name__.startswith('Django')]
REQUEST_FIELD_KEY = 'field'
REQUEST_VALUE_KEY = 'field-value'

def home(request):
    context = {
        'tables': TABLES,
        'header': [],
        'data': []
    }
    if request.method == 'POST':
        table_name = request.POST.get('table', None)
        model = apps.get_model('webui', table_name)
        context['header'] = [x.name for x in model._meta.get_fields() if isinstance(x, Field)]
        context['data'] = [x.__dict__ for x in model.objects.all()]
    return render(request, 'webui/home.html', context)

def about(request):
    return render(request, 'webui/about.html')
