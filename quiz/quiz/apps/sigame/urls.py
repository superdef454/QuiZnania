from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "sigame"), # Выбор раздела
    path('game/end/', views.end, name = 'end'),
    path('game/<section>/', views.type_selection, name = 'type_selection'), # Выбор игры
    path('game/<section>/<type>/', views.round_selection, name = 'round_selection'), # Выбор раунда
    path('game/<section>/<type>/<int:round>/', views.game, name = 'game'), # игра
]