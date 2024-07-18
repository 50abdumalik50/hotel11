from django.core.exceptions import ValidationError
from django.db import models


class Restaurant(models.Model):
    title = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=300
    )


class Hour(models.Model):
    meal = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    meal_type = models.CharField(
        max_length=20,
        choices=meal,
    )
    startDate = models.TimeField(
        null=True,
    )
    endDate = models.TimeField(
        null=True,
    )


class Restaurant_Menu(models.Model):
    menu = (
        ('Starters', 'Starters'),
        ('Mains', 'Mains'),
        ('Salads', 'Salads'),
        ('Beverage', 'Beverage'),
        ('Dessert', 'Dessert'),
    )
    menu_type = models.CharField(
        max_length=20,
        choices=menu,
    )
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(
        max_digits=1000,
        decimal_places=2,
    )
    photo = models.ImageField(
        upload_to='menu_photos/',
        blank=True,
        null=True,
    )

    def clean(self):
        if Restaurant_Menu.objects.filter(name=self.name, menu_type=self.menu_type).exists():
            raise ValidationError(f'Dish with name "{self.name}" already exists in the "{self.menu_type}" category.')

    def clean(self):
        if Restaurant_Menu.objects.filter(name=self.name, menu_type=self.menu_type).exclude(id=self.id).exists():
            raise ValidationError(f'Dish with name "{self.name}" already exists in the "{self.menu_type}" category.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

