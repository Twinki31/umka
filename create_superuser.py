import os
import django
from django.contrib.auth import get_user_model
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password)
    print(f"Суперпользователь {username} создан.")
else:
    print(f"Суперпользователь {username} уже существует.")
