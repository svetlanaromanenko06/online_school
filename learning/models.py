from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название курса')
    preview = models.ImageField(verbose_name='изображение курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')

    def __str__(self):
        return f'{self.title}, {self.description}, {self.preview}'

    class Meta:

        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока')
    preview = models.ImageField(upload_to='lessons/', verbose_name='изображение урока', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.preview}'

    class Meta:

        verbose_name = "урок"
        verbose_name_plural = "уроки"



