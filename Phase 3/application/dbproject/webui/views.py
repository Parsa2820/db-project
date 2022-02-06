from shutil import ExecError
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from matplotlib.style import context

TABLES = [x for x in connection.introspection.table_names() if not x.startswith('auth_') and not x.startswith('django_')]
REQUEST_FIELD_KEY = 'field'
REQUEST_VALUE_KEY = 'field-value'

def home(request):
    context = {
        'tables': TABLES,
        'header': [],
        'data': []
    }
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        try:
            user = str(search_id)
            # fill context
        except Exception:
            return HttpResponse("Not a query!")
    return render(request, 'webui/home.html', context)

def about(request):
    return render(request, 'webui/about.html')
