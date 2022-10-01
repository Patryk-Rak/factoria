from django.contrib import admin
from .models import Client
# Register your models here.


class AdminClient(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'phone', 'picture', 'date_of_birth', )
    search_fields = ('id', 'email')
    ordering = ('id',)
    list_filter = ('id', 'name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'picture', 'password')
        }),
        ('Permission', {
            'fields': ('email', )
        }),
    )


admin.site.register(Client, AdminClient)