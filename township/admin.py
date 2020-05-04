from django.contrib import admin


from .resources import StateResource, TownResource
from import_export.admin import ImportExportModelAdmin
from .models import State, Township


# Register your models here.


class StateAdmin(ImportExportModelAdmin):
    resource_class = StateResource


admin.site.register(State, StateAdmin)


class TownAdmin(ImportExportModelAdmin):
    resource_class = TownResource


admin.site.register(Township, TownAdmin)
