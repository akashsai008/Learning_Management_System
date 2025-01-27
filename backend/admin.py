from django.contrib import admin
from .models import *
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import redirect
from . import views
# Register your models here.


def custom_button_action(modeladmin, request, queryset):
    # Perform your custom action here
    return HttpResponse("Button clicked!")


custom_button_action.short_description = "Custom Button Action"


class VideoAdmin(admin.ModelAdmin):   

    actions = [custom_button_action]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Redirect or block the 'add' URL
            path('add/', self.admin_site.admin_view(views.add_video)),
        ]
        return custom_urls + urls
    

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Video,VideoAdmin)
