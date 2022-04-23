import django.db.models
from django.db.models import QuerySet, Q

from .models import Table
from .filterform import ToFilter
from .sortform import ToSort


def sort_processing(table: django.db.models.QuerySet, sortform: ToSort) -> QuerySet:
    """
    Sort table by conditions from ToSort form.
    :param table: queryset of Table.objects.all() to sort
    :param sortform: data from ToSort form
    :return: sorted table
    """
    if sortform.is_valid():
        sort_dict = sortform.cleaned_data['sort_form']
        if sort_dict:
            table = table.order_by(sort_dict)
            return table
    return table.order_by('id')


def filter_processing(table: django.db.models.QuerySet, filterform: ToFilter) -> QuerySet:
    """
    Filter table by conditions from ToFilter form.
    :param table: queryset of Table.objects.all() to filter
    :param filterform: data from ToFilter form
    :return: sorted table
    """
    if filterform.is_valid():
        choices = filterform.cleaned_data['choices']
        conditions = filterform.cleaned_data['conditions']
        table_categories = filterform.cleaned_data['table_categories']

        match table_categories:
            case 'amount':
                match conditions:
                    case 'lt':
                        table = table.filter(amount__lt=choices)
                    case 'gt':
                        table = table.filter(amount__gt=choices)
                    case 'contain':
                        table = table.filter(amount__icontains=choices)
                    case 'equal':
                        table = table.filter(amount__exact=choices)
            case 'distance':
                match conditions:
                    case 'lt':
                        table = table.filter(distance__lt=choices)
                    case 'gt':
                        table = table.filter(distance__gt=choices)
                    case 'contain':
                        table = table.filter(distance__icontains=choices)
                    case 'equal':
                        table = table.filter(distance__exact=choices)
            case 'name':
                if conditions == 'equal' or conditions == 'contain':
                    table = table.filter(Q(name__icontains=choices) | Q(name__exact=choices))

    return table


def general_processing(sortform: ToSort, filterform: ToFilter) -> django.db.models.QuerySet:
    """
    Process data with filtering and sorting.
    :param sortform: data from ToSort from
    :param filterform: data from ToFilter form
    :return: processed table
    """
    table: QuerySet[Table] = Table.objects.all()
    table = filter_processing(table, filterform)
    table = sort_processing(table, sortform)

    return table
