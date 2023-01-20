from django.shortcuts import render, get_object_or_404
from .models import Tile
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
# Create your views here.s

def tiles(request):
    tiles = Tile.objects.order_by('-created_date')
    paginator = Paginator(tiles, 4)
    page = request.GET.get('page')
    paged_tiles = paginator.get_page(page)

    model_search = Tile.objects.values_list('model', flat=True).distinct()
    city_search = Tile.objects.values_list('city', flat=True).distinct()
    year_search = Tile.objects.values_list('year', flat=True).distinct()
    body_style_search = Tile.objects.values_list('body_style', flat=True).distinct()

    data = {
        'Tiles': paged_tiles,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'tiles/tiles.html', data)

def tile_detail(request, id):
    single_tile = get_object_or_404(Tile, pk=id)

    data = {
        'single_tile': single_tile,
    }
    return render(request, 'tiles/tile_detail.html', data)


def tilesearch(request):
    tiles = Tile.objects.order_by('-created_date')
    model_search = Tile.objects.values_list('model', flat=True).distinct()
    city_search = Tile.objects.values_list('city', flat=True).distinct()
    year_search = Tile.objects.values_list('year', flat=True).distinct()
    body_style_search = Tile.objects.values_list('body_style', flat=True).distinct()
  
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tiles = tiles.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            tiles = tiles.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tile = tiles.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            tiles = tiles.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            tiles = tiles.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            tiles = tiles.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'tiles': tiles,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'tiles/tilesearch.html', data)

# Create your views here.
