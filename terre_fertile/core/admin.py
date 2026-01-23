from django.contrib import admin
from .models import HomePage, CarouselItem


class CarouselItemInline(admin.TabularInline):
    model = CarouselItem
    fk_name = 'homepage'
    extra = 1
    fields = ('ordre', 'image', 'titre', 'description', 'actif')


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    inlines = [CarouselItemInline]
    list_display = ('__str__', 'updated_at')


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'homepage', 'ordre', 'actif')
    list_editable = ('ordre', 'actif')
    list_filter = ('actif',)
    ordering = ('ordre',)
