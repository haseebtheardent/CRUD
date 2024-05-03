from django.contrib import admin
from .models import RecordTable

class RecordTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'membership']
    list_filter = ['membership']
    search_fields = ['first_name', 'last_name', 'email', 'phone']

admin.site.register(RecordTable, RecordTableAdmin)