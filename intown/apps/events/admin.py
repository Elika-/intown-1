from django.contrib import admin

from .models import Event
from .models import EventType
from .models import EventOpenHours


class OpenHoursInline(admin.StackedInline):
    model = EventOpenHours
    choices = 7


class EventAdmin(admin.ModelAdmin):
    inlines = [OpenHoursInline]


class EventTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
