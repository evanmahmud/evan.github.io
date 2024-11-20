'''from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),
]'''




# portfolio_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),  # Comment this out temporarily
    # path('project/<int:project_id>/', views.project_detail, name='project_detail'),  # Comment this out
]