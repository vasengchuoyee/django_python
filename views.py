from django.shortcuts import render
from django.http import HttpResponse


# def base(request):
#     return render(request, 'base.html')

def index(request):
    return render(request, 'forest/index.html' )
# def index(request):
#     data = {
#         'title': 'django framwork',
#         'message': 'learning with django',
#         'numbers': ['I','L','O','V','E','Y','O','U']
#     }
#     return render(request, 'forest/index.html', data)

def about(request):
    return render(request, 'forest/about.html')

def product(request):
    return render(request, 'forest/product.html')

    
def search(request, keyword, page):
    return HttpResponse(
        f'<h1>searching : {keyword} page: {page}</h1>'
        'button to searching here'
    )

def map(request):
    type = request.GET.get('type')
    lat = request.GET.get('lat')
    log = request.GET.get('log')
    zoom = request.GET.get('zoom')

    return HttpResponse(f'<h2>type: {type} lat: {lat} log: {log} zoom: {zoom}</h2>')