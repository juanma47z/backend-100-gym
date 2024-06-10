from django.contrib import admin
from .models import Coach, Customer

class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'cell_phone')
    search_fields = ('name', 'last_name', 'email')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email', 'cell_phone')
    search_fields = ('name', 'last_name', 'email')

admin.site.register(Coach, CoachAdmin)
admin.site.register(Customer, CustomerAdmin)
