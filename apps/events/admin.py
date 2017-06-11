from django.contrib import admin
from apps.events.models import TypeEventModel,EventModel,TypeLocation,ImagesEvent,GalleryEvent,EventSchedule,RequestAssistance
# Register your models here.
admin.site.register(TypeEventModel)
admin.site.register(EventModel)
admin.site.register(TypeLocation)
admin.site.register(ImagesEvent)
admin.site.register(GalleryEvent)
admin.site.register(EventSchedule)
admin.site.register(RequestAssistance)
