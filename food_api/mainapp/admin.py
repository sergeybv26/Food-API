from django.contrib import admin

from mainapp.models import FoodCategory, Food


@admin.register(FoodCategory, Food)
class FoodAdmin(admin.ModelAdmin):
    pass
