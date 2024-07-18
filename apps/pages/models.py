import os
from django.core.exceptions import ValidationError
from django.db import models
from utils.image_path import upload_teams


class Service(models.Model):
    name = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=100
    )


class Team(models.Model):
    name = models.CharField(
        max_length=50,
    )
    occupation = models.CharField(
        max_length=50,
    )
    image_for_team = models.ImageField(
        upload_to="team_media/",
        blank=True,
        null=True,
    )

    def clean(self):
        if Team.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError(f'Team with name "{self.name}" already exists.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name} ({self.occupation})"


class Facilities(models.Model):
    name = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=100
    )


class Contact(models.Model):
    name = models.CharField(
        max_length=50
    )
    number = models.CharField(
        max_length=50
    )
    email = models.EmailField()
    subject = models.CharField(
        max_length=50
    )


class About(models.Model):
    title = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=100
    )
