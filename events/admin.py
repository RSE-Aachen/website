from django.contrib import admin
from .models import Event, EventHost, EventType

admin.site.register(Event)
admin.site.register(EventHost)
admin.site.register(EventType)
