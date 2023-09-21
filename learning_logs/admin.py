from django.contrib import admin
from learning_logs.models import Topic, Entry, Locations, UserProfile
from .forms import UserProfileAdminForm

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Locations)

#Extra modifiying for users
class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileAdminForm
    list_display = ('user', 'location')
    list_filter = ('location',)  # You can add more filters as needed

admin.site.register(UserProfile, UserProfileAdmin)
