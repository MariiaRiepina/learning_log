from django.contrib import admin

from learning_logs.models import Topic, Entry, Locations

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Locations)
