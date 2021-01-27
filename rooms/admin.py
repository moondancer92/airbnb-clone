from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definiton """

    pass


@admin.register(models.Photo)
class PhotoAdimin(admin.ModelAdmin):
    """Photo Admin Definition """

    pass
