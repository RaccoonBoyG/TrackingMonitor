from django.db import models

class Track(models.Model):
    username = models.CharField("Имя пользователя", blank=True, null=True, max_length=512)
    event_type = models.CharField("Тип события", null=True, blank=True, max_length=512)
    ip = models.CharField("IP адрес пользователя", blank=True, null=True, max_length=512)
    agent = models.CharField("Информация о браузере", blank=True, null=True, max_length=512)
    description = models.TextField("Описание платформы", blank=True, null=True)
    ogrn = models.CharField("ОГРН", blank=True, null=True, max_length=512)
    contacts = models.TextField("Контакты", blank=True, null=True) 