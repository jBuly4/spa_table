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
    pages = Paginator(processing_results, 2).get_page(page_num)

    context = {
        'filter': to_filter,
        'sort': to_sort,
        'table': pages,
    }

    return render(client, 'table/base.html', context=context)
