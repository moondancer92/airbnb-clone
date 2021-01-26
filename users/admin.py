from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class CustomAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets: tuple
    fieldsets = UserAdmin.fieldsets + (
        (
            "Customprofile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


admin.site.register(models.User, CustomAdmin)
