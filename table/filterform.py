import django.forms
from django.forms import Form


class ToFilter(Form):
    """Filtering form."""

    choices = django.forms.CharField(
            label='Make a choice',
            widget=django.forms.TextInput(attrs={
                'placeholder': 'Type a number or a name to filter'
            }),
            required=False
    )

    table_categories = django.forms.ChoiceField(
            label='Categories',
            choices=[
                ['distance', 'Distance'],
                ['amount', 'Amount'],
                ['name', 'Name']
            ],
            required=False
    )

    conditions = django.forms.ChoiceField(
            label='Condition',
            choices=[
                ['lt', 'Less than'],
                ['gt', 'Greater than'],
                ['equal', 'Equal'],
                ['contain', 'Contain'],
            ],
            required=False
    )