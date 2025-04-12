from django.contrib import admin
from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    def __str__(self):
        return super().__str__()

admin.site.register(contact ,ContactAdmin)