# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем зависимости для приложения
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем исходный код приложения в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Указываем команду для запуска приложения
CMD ["python", "manage.py", "runserver"]