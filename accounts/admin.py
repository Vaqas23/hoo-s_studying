from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "year", "majors_minors",
                    "preferred_meeting_location")
    search_fields = ("user__username", "user__email", "majors_minors")
    list_filter = ("year", "gender")
