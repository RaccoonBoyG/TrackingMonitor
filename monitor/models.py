from django.db import models

#Модель трэклога
class Track(models.Model):
    username = models.CharField("Имя пользователя", blank=True, null=True, max_length=512)
    event_type = models.CharField("Тип события", null=True, blank=True, max_length=512)
    ip = models.CharField("IP адрес пользователя", blank=True, null=True, max_length=512)
    agent = models.CharField("Информация о браузере", blank=True, null=True, max_length=512)
    host = models.CharField("Имя хоста", blank=True, null=True, max_length=512)
    referer = models.URLField("Осуществяемый переход", blank=True, null=True)
    accept_language = models.CharField("Язык", blank=True, null=True, max_length=512)
    event = models.CharField("Собыите", blank=True, null=True, max_length=512)
    event_source = models.CharField("Server", blank=True, null=True, max_length=512)
    context = models.ManyToManyField("TrackCourse", verbose_name="Контекст курса", blank=True, null=True)
    time = models.CharField("Время события", blank=True, null=True, max_length=512)
    page = models.CharField("Страница", blank=True, null=True, max_length=512)

    def __str__(self):
        return f"Трэкинг: {self.host}"

    class Meta:
        verbose_name = 'Трэкинг'
        verbose_name_plural = 'Трэкинг'

class TrackCourse(models.Model):
    user_id = models.CharField("ИД пользователя", blank=True, null=True, max_length=512)
    org_id  = models.CharField("ИД организации", blank=True, null=True, max_length=512)
    course_id = models.CharField("ИД курса", blank=True, null=True, max_length=512)
    path = models.TextField("Путь перехода", blank=True, null=True)

    def __str__(self):
        return self.course_id

    class Meta:
        verbose_name = 'Трэкинг в курсе'
        verbose_name_plural = 'Трэкинг в курсе'