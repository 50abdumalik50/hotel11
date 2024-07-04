from django.contrib import admin

from apps.rooms.models import Room, Booking

admin.site.register(Room)
admin.site.register(Booking)

#
# class RoomImageInline(admin.TabularInline):
#     model = RoomImage
#     extra = 1
#
#
# @admin.register.html(RoomImage)
# class RoomImageAdmin(admin.ModelAdmin):
#     list_display = ['image']

