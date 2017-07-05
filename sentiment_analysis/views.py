from django.shortcuts import render


# load index page
def index(request):
    return render(request, 'sentiment_analysis/base.html')


def about(request):
    return render(request, 'sentiment_analysis/about.html')
