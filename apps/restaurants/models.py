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
    # description = models.TextField(max_length=100)


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
    # Menu = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(
        max_digits=1000,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.name} ({self.menu_type})"

