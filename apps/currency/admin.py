from django.contrib import admin
from .models import Portfolio, AssetsUser, Asset, AssetTimeline
# Register your models here.
admin.site.register(AssetTimeline)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'cod', 'price']


@admin.register(AssetsUser)
class AssetsUserAdmin(admin.ModelAdmin):
    list_display = ['assets_in', 'portfolio', 'balance']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['user', 'total']
