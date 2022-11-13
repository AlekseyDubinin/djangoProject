from django.contrib import admin

from ads.models import Categories, Ad, Location, User


admin.site.register(Categories)
admin.site.register(Location)
admin.site.register(Ad)
admin.site.register(User)
