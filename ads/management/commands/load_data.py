from django.core.management.base import BaseCommand
from ads.models import Ad, Categories, Location, User
import json


class Command(BaseCommand):
    with open('datasets/category.json', 'r') as file:
        new_file = json.load(file)
    for i in new_file:
        new_categories = Categories(
            name=i['name'],
        )
        new_categories.save()

    with open('datasets/location.json', 'r') as file:
        new_file = json.load(file)
    for i in new_file:
        new_categories = Location(
            name=i['name'],
            lat=i['lat'],
            lng=i['lng'],
        )
        new_categories.save()

    with open('datasets/user.json', 'r') as file:
        new_file = json.load(file)
    for i in new_file:
        new_categories = User(
            first_name=i['first_name'],
            last_name=i['last_name'],
            username=i['username'],
            password=i['password'],
            role=i['role'],
            age=i['age'],
        )
        new_categories.save()

    def handle(self, *args, **kwargs):
        with open('datasets/ad.json', 'r') as file:
            new_file = json.load(file)
        for i in new_file:
            new_ads = Ad(
                name=i['name'],
                author_id=i['author_id'],
                price=i['price'],
                description=i['description'],
                is_publisher=i['is_published'].lower().title(),
                image=i['image'],
                category_id=i['category_id'],

            )
            new_ads.save()


