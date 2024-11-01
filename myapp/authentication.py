# your_app/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class HardCodedTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Получаем токен из заголовка Authorization
        token = request.headers.get("Authorization")

        # Проверяем, чтобы токен соответствовал захардкоженному токену
        if token == f"Token {settings.API_HARD_CODED_TOKEN}":
            return (None, None)  # Не требуется пользовательская модель

        # Если токен не совпадает, вызываем ошибку аутентификации
        raise AuthenticationFailed("Invalid token")
