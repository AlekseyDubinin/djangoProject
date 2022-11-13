from django.contrib import admin
from django.urls import path, include
from ads.views import index, CatListView, AdListView, CatDetailView, AdDetailView,\
    CategoryUpdateView, AdDeleteView, AdUpdateView, CatDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ads.urls')),
    path('user/', include('users.urls'))

]
