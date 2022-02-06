from shutil import ExecError
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from matplotlib.style import context



def home(request):
    context = {
        'tables': connection.introspection.table_names(),
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
