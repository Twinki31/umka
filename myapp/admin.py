from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'tg_acc', 'chatid', 'created_dttm', 'balance', 'meeting_count')  # Поля, отображаемые в списке
    search_fields = ('username', 'tg_acc', 'chatid')  # Поля, по которым можно искать
    list_filter = ('created_dttm',)  # Фильтрация по дате создания
