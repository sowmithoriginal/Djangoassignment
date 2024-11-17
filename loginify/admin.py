from django.contrib import admin
from .models import UserDetails

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # Fields to display in the admin panel
    search_fields = ('username', 'email')  # Add search functionality
