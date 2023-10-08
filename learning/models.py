from django.db import models
from users.models import NULLABLE, User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название курса')
    preview = models.ImageField(verbose_name='изображение курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса', **NULLABLE)

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


    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    def __str__(self):
        return f'{self.title}, {self.description}, {self.preview}'

    class Meta:

        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Payment(models.Model):
    payment_choice = (
        ('cash', 'наличные'),
        ('transfer', 'перевод на счет'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='урок')
    amount = models.PositiveIntegerField(verbose_name='сумма оплаты')
    pay_method = models.CharField(max_length=50, choices=payment_choice, verbose_name='метод оплаты')

    def __str__(self):
        return f'{self.payment_date}, {self.payment_choice}, {self.pay_method}, {self.course if self.course else self.lesson}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


