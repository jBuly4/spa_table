from django.db import models


# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=150, name='name')
    amount = models.PositiveIntegerField(name='amount')
    distance = models.FloatField(name='distance')
    date = models.DateField(auto_now_add=True, name='date')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
