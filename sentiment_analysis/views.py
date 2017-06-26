from django.shortcuts import render


# load index page
def index(request):
    country = request.GET.get('country', '')
    return render(request, 'sentiment_analysis/base.html', {'country': country})


def about(request):
    return render(request, 'sentiment_analysis/about.html')
