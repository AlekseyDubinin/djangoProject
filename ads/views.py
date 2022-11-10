import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from ads.models import Ads, Categories


def index(request):
    return JsonResponse({"status": "ok"}, safe=False, status=200)


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Cat(View):
    def get(self, request):
        data = Categories.objects.all()
        list_data = []
        for category in data:
            list_data.append(
                {
                    'id': category.id,
                    'name': category.name
                }
            )
        return JsonResponse(list_data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new = Categories(
                name=data['name'],
        )
        new.save()
        return JsonResponse({"id": new.id, 'name': new.name}, safe=False, status=200)


class NewCat(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        try:
            new = self.get_object()
        except Http404:
            return JsonResponse({'status': '404 Not Found'}, status=404)
        return JsonResponse(
            {
                'id': new.id,
                'name': new.name
            }
        )


class Ad(View):
    def get(self, request):
        data = Ads.objects.all()
        list_data = []
        for category in data:
            list_data.append(
                {
                    'id': category.id,
                    'name': category.name,
                    'author': category.author,
                    'price': category.price

                }
            )
        return JsonResponse(list_data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new = Ads(
            name=data.name,
            author=data.author,
            price=data.price,
            description=data.description,
            address=data.address,
            is_published=data.is_publisher
        )
        new.save()
        return JsonResponse(
            {
                'id': new.id,
                'name': new.name,
                'author': new.author,
                'price': new.price,
                'description': new.description,
                'address': new.address,
                'is_published': new.is_publisher,
            }, safe=False, status=200
        )


class NewAd(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            new = self.get_object()
        except Http404:
            return JsonResponse({'status': '404 Not Found'}, status=404)
        return JsonResponse(
            {
                'id': new.id,
                'name': new.name,
                'author': new.author,
                'price': new.price,
                'description': new.description,
                'address': new.address,
                'is_published': new.is_publisher,
            }, safe=False, status=200
        )
