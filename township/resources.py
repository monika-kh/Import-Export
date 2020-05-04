from django.http import HttpResponse
from import_export import resources, fields, widgets
from .models import State, Township


class StateResource(resources.ModelResource):
    class Meta:
        model = State
        fields = ('id', 'state_name', 'number')
        skip_unchanged = True
        report_skipped = True


class TownResource(resources.ModelResource):
    class Meta:
        model = Township
        fields = ('id', 'name', 'state')
        skip_unchanged = True
        report_skipped = True