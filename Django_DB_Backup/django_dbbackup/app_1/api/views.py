from django.core.management import call_command
from django.http import HttpResponse

def trial(request):
    call_command('dbbackup')
    return HttpResponse('db create')