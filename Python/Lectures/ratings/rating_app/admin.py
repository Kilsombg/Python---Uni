from django.contrib import admin
from .models import Information

# Register your models here.


class InformationAdmin(admin.ModelAdmin):
    fields = ['title', 'text']


admin.site.register(Information, InformationAdmin)
