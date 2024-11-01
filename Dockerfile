# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем зависимости для приложения
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем исходный код приложения в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

EXPOSE 8000

# Указываем команду для запуска приложения
CMD ["sh", "-c", "python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"]

