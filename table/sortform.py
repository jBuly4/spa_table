import django.forms
from django.forms import Form


class ToSort(Form):
    """Sorting form."""

    sort_form = django.forms.ChoiceField(
            label='Make sort by category',
            choices=[
                ['distance', 'Distance'],
                ['amount', 'Amount'],
                ['name', 'Name']
            ],
            required=False
    )