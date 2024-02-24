from django.contrib import admin
from .models import *

class Profile_inline(admin.StackedInline):
    model = User_profile

class Admin(admin.ModelAdmin):
    model = User
    list_display = ('email','username','date_joined','is_superuser')
    search_fields = ('email','username','first_name')
    fieldsets = (
        ('User settings', {'fields': ('email', 'username','password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
    ) 
    inlines = [Profile_inline]

admin.site.unregister(User)
admin.site.register(User, Admin)