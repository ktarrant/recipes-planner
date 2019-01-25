from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import *

# Register your models here.
class IngredientAdminInline(admin.TabularInline):
    model = Ingredient

class RecipeAdmin(PageAdmin):
    inlines = (IngredientAdminInline, )
    pass

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)