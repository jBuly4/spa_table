from django.core.paginator import Paginator
from django.shortcuts import render

from .filterform import ToFilter
from .processing import general_processing
from .sortform import ToSort


# Create your views here.

def index_view(client):
    to_filter = ToFilter(client.GET)
    to_sort = ToSort(client.GET)

    processing_results = general_processing(
            to_sort,
            to_filter
    )

    page_num = client.GET.get('page_num', 1)
    # pages = Paginator(processing_results, 2).get_page(page_num)
    # first_page = pages.page
    # page_range = pages.page_range
    pages = Paginator(processing_results, 10)
    first_page = pages.page(1).object_list
    page_range = pages.page_range

    context = {
        'filter': to_filter,
        'sort': to_sort,
        'table': pages.get_page(page_num),
        'page_range': page_range,
    }

    return render(client, 'table/base.html', context=context)
