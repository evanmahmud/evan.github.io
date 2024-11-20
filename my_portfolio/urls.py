'''from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Import HttpResponse
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),  # You can uncomment this later
    path('', lambda request: HttpResponse("Evan's Portfolio"), name='home'),
    path('', include('portfolio_app.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







'''



from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Keep this line only once
    path('', include('portfolio_app.urls')),
    path('', lambda request: HttpResponse("Evan's Portfolio"), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)