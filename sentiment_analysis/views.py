from django.shortcuts import render
from rest_framework import generics
from .models import Data
from .serializers import DataSerializer


class DataViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Data.objects.all().order_by('date')
    serializer_class = DataSerializer


# load index page
def index(request):
    data = Data.objects.latest('date')
    return render(request, 'sentiment_analysis/base.html', {'data': data})


def about(request):
    return render(request, 'sentiment_analysis/about.html')
