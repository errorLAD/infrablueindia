from django.shortcuts import render, get_object_or_404
from .models import Marble
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
# Create your views here.
def marbles(request):
    marbles = Marble.objects.order_by('-created_date')
    paginator = Paginator(marbles, 4)
    page = request.GET.get('page')
    paged_marbles = paginator.get_page(page)

    model_search = Marble.objects.values_list('model', flat=True).distinct()
    city_search = Marble.objects.values_list('city', flat=True).distinct()
    year_search = Marble.objects.values_list('year', flat=True).distinct()
    body_style_search = Marble.objects.values_list('body_style', flat=True).distinct()

    data = {
        'marbles': paged_marbles,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'marbles/marbles.html', data)

def marble_detail(request, id):
    single_marble = get_object_or_404(Marble, pk=id)

    data = {
        'single_marble': single_marble,
    }
    return render(request, 'marbles/marble_detail.html', data)


def marblesearch(request):
    marbles = Marble.objects.order_by('-created_date')

    model_search = Marble.objects.values_list('model', flat=True).distinct()
    city_search = Marble.objects.values_list('city', flat=True).distinct()
    year_search = Marble.objects.values_list('year', flat=True).distinct()
    body_style_search = Marble.objects.values_list('body_style', flat=True).distinct()
  
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            marbles = marbles.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            marbles = marbles.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            marbles = marbles.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            marbles = marbles.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            marbles = marbles.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            marbles = marbles.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'marbles': marbles,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'marbles/marblesearch.html', data)
