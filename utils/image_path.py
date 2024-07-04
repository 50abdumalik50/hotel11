import os


def upload_rooms(instance, filename):
    return f"rooms/{instance.room.room_type}/{filename}"


def upload_teams(instance, filename):
    return f"teams/{instance.team.name}/{filename}"