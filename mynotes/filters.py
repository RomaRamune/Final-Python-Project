import django_filters

from .models import *

class Categoryfilter(django_filters.FilterSet):

    class Meta:
        model = Note
        fields = ['category', ]

