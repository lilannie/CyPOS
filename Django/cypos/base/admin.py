from django.contrib import admin

from .models import TestUsers
# Register your models here.


# Changes how Users display in Admin Interface
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'email']

admin.site.register(TestUsers, UsersAdmin)

