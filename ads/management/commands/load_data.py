from django.core.management.base import BaseCommand
from ads.models import Ads, Categories
import json


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('datasets/ads.json', 'r') as file:
            new_file = json.load(file)
        for i in new_file:
            new_ads = Ads(
                name=i['name'],
                author=i['author'],
                price=i['price'],
                description=i['description'],
                address=i['address'],
                is_publisher=i['is_published'].lower().title(),
            )
            new_ads.save()

        with open('datasets/categories.json', 'r') as file:
            new_file = json.load(file)
        for i in new_file:
            new_categories = Categories(
                name=i['name'],
            )
            new_categories.save()

