from django.urls import path
from .views import CreateUser , UserDetail, BalanceView, UpdateUser, BalanceUpdate

urlpatterns = [
    path('api/users/', CreateUser.as_view(), name='create_user'),  # Создание нового пользователя
    path('api/users/', UserDetail.as_view(), name='user_detail'),  # Получение информации о пользователе
    path('api/users/balance/', BalanceView.as_view(), name='balance'), # Получение баланса пользователя
    path('api/users/balance1/', BalanceUpdate.as_view(), name='update_balance'), 
    path('api/users/', UpdateUser.as_view(), name='update_user'),  # Обновление пользователя
]
