from django.urls import path
from .views import CreateUser, UserDetail, AddBalanceView, BalanceView

urlpatterns = [
    path('users/', CreateUser.as_view(), name='create_user'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('users/<int:pk>/add_balance/', AddBalanceView.as_view(), name='add_balance'),
    path('users/<int:pk>/balance/', BalanceView.as_view(), name='get_balance'),
]
