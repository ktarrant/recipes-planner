from django.db import models

from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField

from .fields import DIFFICULTIES, UNITS

class Recipe(Page):
    """
    Implements the recipe type of page with all recipe fields
    """
    portions = models.IntegerField("Portions", blank=True, null=True)
    difficulty = models.IntegerField("Difficulty", choices=DIFFICULTIES, blank=True, null=True)
    source = models.URLField("Source", blank=True, null=True, help_text="URL of the source recipe")
    instructions = RichTextField("Instructions")

class Ingredient(Orderable):
    """
    Provides ingredient fields for managing recipe content and making
    it searchable.
    """
    recipe = models.ForeignKey("Recipe", verbose_name="Recipe", related_name="ingredients")
    quantity = models.FloatField("Quantity", null=True)
    unit = models.IntegerField("Unit", choices=UNITS, blank=True, null=True)
    ingredient_name = models.CharField("Ingredient Name", max_length=100)
    ingredient_recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    note = models.CharField("Note", max_length=200, blank=True, null=True)