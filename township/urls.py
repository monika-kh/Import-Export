from django.urls import path
from . import views

urlpatterns = [
    path('state/', views.StateView.as_view(), name='state'),
    path('<int:state_id>/township/', views.TownshipView.as_view(), name='town'),
]
