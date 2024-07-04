import os
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


# class TeamImage(models.Model):
#     team = models.ForeignKey(
#         Team, on_delete=models.CASCADE,
#         related_name='images',
#     )
#     image = models.ImageField(
#         upload_to=upload_teams,
#     )
#
#     def delete(self, using=None, keep_parents=False):
#         os.remove(self.image.path)
#         super().delete(using=None, keep_parents=False)
#
#     def __str__(self):
#         return f"{self.image.url}"


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
    # message = models.TextField(
    #     max_length=100
    # )


class About(models.Model):
    title = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=100
    )
