from django.shortcuts import render

from .models import Settings

# Create your views here.
def index(request):
   
    settings = Settings.objects.latest('id')
    return render(request, 'index.html', locals())

