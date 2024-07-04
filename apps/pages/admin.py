from django.contrib import admin

from apps.pages.models import Service, Team

admin.site.register(Service)
admin.site.register(Team)


# class RoomImageInline(admin.TabularInline):
#     model = TeamImage
#     extra = 1
#
#
# @admin.register(TeamImage)
# class RoomImageAdmin(admin.ModelAdmin):
#     list_display = ['image']
