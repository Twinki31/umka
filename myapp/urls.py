from django.urls import path
from .views import CreateUser , UserDetail, BalanceView, UpdateUser, AddBalanceView

urlpatterns = [
    path('api/users/', CreateUser.as_view(), name='create_user'),  # Создание нового пользователя
    path('api/users/', UserDetail.as_view(), name='user_detail'),  # Получение информации о пользователе
    path('api/users/funds/', BalanceView.as_view(), name='user_funds'),  # Получение баланса пользователя
    path('api/users/update/', UpdateUser.as_view(), name='update_user'),  # Обновление пользователя
    path('api/users/deposit/', AddBalanceView.as_view(), name='user_deposit'),  # Добавление баланса пользователю
]
