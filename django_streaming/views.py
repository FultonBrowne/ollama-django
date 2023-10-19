from django.shortcuts import render


def index(request):
    context = {'page_name': 'landing_page'}
    return render(request, 'index.html', context)