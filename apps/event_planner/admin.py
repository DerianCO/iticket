from django.contrib import admin
from apps.event_planner.models import EventPlannerModel,SponsorModel,GuestsModels,ShellersGroupModel,ShellerModel
# Register your models here.
admin.site.register(EventPlannerModel)
admin.site.register(SponsorModel)
admin.site.register(GuestsModels)
admin.site.register(ShellersGroupModel)
admin.site.register(ShellerModel)