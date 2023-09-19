from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('locations/', views.LocationsListView.as_view(), name='location_list'),
    path('locations/<int:pk>/', views.LocationsDetailView.as_view(), name='location_detail'),
    # Добавьте другие маршруты по необходимости
]


