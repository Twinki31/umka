from django.urls import path
from .views import CreateUser , UserDetail, BalanceView, UserDetailUpdate

urlpatterns = [
    path('api/users/', CreateUser.as_view(), name='create_user'),  # Создание нового пользователя
    path('api/users/get/', UserDetail.as_view(), name='user_detail'),  # Получение информации о пользователе
    path('api/users/update/', UserDetailUpdate.as_view(), name='user_detail_update'),  # Получение информации о пользователе
    path('api/users/balance/', BalanceView.as_view(), name='balance'), # Получение баланса пользователя
]
