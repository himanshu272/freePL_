from django.contrib import admin
from import_export import resources
from app.models import *
# Register your models here.
from import_export.admin import ImportExportActionModelAdmin

class PlayerResource(resources.ModelInstanceLoader):

    class Meta:
        model = Player

class leaderboardmodeladmin(admin.ModelAdmin):
    list_display = ['_username','_name','_email','_score']

class PlayerAdmin(ImportExportActionModelAdmin):
    resource_class = PlayerResource
    pass

admin.site.register(Player)
admin.site.register(Person)
admin.site.register(PersontoPM)
admin.site.register(Match)
admin.site.register(PlayertoMatch)
