from django.shortcuts import render
from multiplecheckbox.models import colornames

def displaycolors(request):
    result = colornames.objects.all()
    return render(request, 'index.html', {"colornames":result})