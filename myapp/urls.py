from django.urls import path
from .views import CreateUser , UserDetail, BalanceView, UpdateUser, AddBalanceView

urlpatterns = [
    path('api/users/', CreateUser.as_view(), name='create_user'),  # Создание нового пользователя
    path('api/users/<int:id>/', UserDetail.as_view(), name='user_detail'),  # Получение информации о пользователе
    path('api/users/<int:id>/funds/', BalanceView.as_view(), name='user_funds'),  # Получение баланса пользователя
    path('api/users/<int:id>/update/', UpdateUser.as_view(), name='update_user'),  # Обновление пользователя
    path('api/users/<int:id>/deposit/', AddBalanceView.as_view(), name='user_deposit'),  # Добавление баланса пользователю
]
