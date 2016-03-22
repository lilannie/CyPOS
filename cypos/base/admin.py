from django.contrib import admin

from .models import UserProfile
# Register your models here.


# Changes how Users display in Admin Interface
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'email']

admin.site.register(UserProfile, UsersAdmin)

