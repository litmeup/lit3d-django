from django.contrib import admin
from .models import PortfolioPage
from django.utils.html import format_html

@admin.register(PortfolioPage)
class PortfolioPageAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'section', 
        'date', 
        'year', 
        'is_active', 
        'main_image_preview'
    )
    list_filter = ('section', 'date', 'is_active')
    search_fields = ('title', 'description_short')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Основное', {
            'fields': (
                'title', 
                'slug',
                'section',
                'date',
                'is_active'
            )
        }),
        ('Описания', {
            'fields': (
                'description_short',
                'description_extended',
                'content'
            )
        }),
        #('Изображения', {
        #    'fields': (
        #        'main_image',
        #    )
        #}),
    )
    
    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 100px;" />',
                obj.main_image.url
            )
        return "-"
    main_image_preview.short_description = 'Превью'
    
    def year(self, obj):
        return obj.date.year
    year.short_description = 'Год'
    year.admin_order_field = 'date__year'