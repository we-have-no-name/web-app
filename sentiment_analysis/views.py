from django.shortcuts import render
from .models import Data


# load index page
def index(request):
    data = Data.objects.latest('date')
    return render(request, 'sentiment_analysis/base.html', {'data': data})


def about(request):
    return render(request, 'sentiment_analysis/about.html')
