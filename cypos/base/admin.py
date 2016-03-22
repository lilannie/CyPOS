from django.contrib import admin
# Register your models here.


# Changes how Users display in Admin Interface
class UsersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


