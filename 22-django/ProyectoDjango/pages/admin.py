from django.contrib import admin
from .models import Page

#Configuracion extra
class PageAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible','created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin)

#configuracion del panel
title = "Proyecto con Django"
subtitle = "Panel  de gestion"

admin.site.site_header = title
admin.site.site_header = title
admin.site.index_title = subtitle