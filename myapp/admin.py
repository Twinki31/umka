from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from io import BytesIO
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'tg_acc', 'chatid', 'created_dttm', 'balance', 'meeting_count', 'last_meeting_date')  # Поля, отображаемые в списке
    search_fields = ('username', 'tg_acc', 'chatid')  # Поля, по которым можно искать
    list_filter = ('created_dttm',)  # Фильтрация по дате создания

    def export_to_excel(self, request, queryset):
        # Создаем новую книгу Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Users"
        
        headers = ['Имя пользователя',
                   'Telegram аккаунт',
                   'ID чата',
                   'Дата создания',
                   'Баланс',
                   'Количество встреч',
                   'Дата последней встречи',
                   'Дата последнего начисления баланса',
                   'Комментари']
        ws.append(headers)
        
        for user in queryset:
            ws.append([
                user.username,
                user.tg_acc,
                user.chatid,
                user.created_dttm.replace(tzinfo=None) if user.created_dttm else None,
                user.balance,
                user.meeting_count,
                user.last_meeting_date.replace(tzinfo=None) if user.last_meeting_date else None,
                user.last_balance_update.replace(tzinfo=None) if user.last_balance_update else None,
                user.comment,
            ])

        output = BytesIO()
        wb.save(output)
        output.seek(0)

        response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="umka-users.xlsx"'

        return response
    
    actions = ['export_to_excel']