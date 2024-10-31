from django.db import models

from django.utils.translation import gettext_lazy as _


class User(models.Model):
    username = models.CharField(_('Имя пользователя'), max_length=150)
    tg_acc = models.CharField(_('Telegram аккаунт'), max_length=255, null=True, blank=True)
    chatid = models.CharField(_('chatid'), max_length=255, unique=True)
    created_dttm = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    balance = models.IntegerField(_('Баланс'), default=0)
    meeting_count = models.IntegerField(_('Количество встреч'), default=0)
    last_meeting_date = models.DateTimeField(_('Дата последней встречи'), null=True, blank=True)
    last_balance_update = models.DateTimeField(_('Дата последнего начисления баланса'), null=True, blank=True)
    comment = models.TextField(_('Комментарий'), null=True, blank=True)
    utm_source = models.CharField(_('Источник кампании utm'), max_length=255, null=True, blank=True)
    utm_medium = models.CharField(_('Тип трафика utm'), max_length=255, null=True, blank=True)
    utm_campaign = models.CharField(_('Название кампании utm'), max_length=255, null=True, blank=True)
    utm_content = models.CharField(_('Идентификатор объявления utm'), max_length=255, null=True, blank=True)
    utm_term = models.CharField(_('Ключевое слово'), max_length=255, null=True, blank=True)
    utm_type_of_report = models.IntegerField(_('Тип отчета'), default=0)
    utm_send_transcription = models.BooleanField(_('Отправлять транскрибацию'), default=False)
