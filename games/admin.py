from django.contrib import admin
from .models import Game, Platform

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_platforms', 'genre', 'rating')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('platform',)

    def get_platforms(self, obj):
        return ", ".join([p.get_name_display() for p in obj.platform.all()])
    get_platforms.short_description = 'Платформи'

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('get_name_display',)