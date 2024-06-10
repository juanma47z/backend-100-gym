from django.contrib import admin
from .models import Services

class ServiciesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'price', 'created', 'updated')
    
admin.site.register(Services, ServiciesAdmin)
