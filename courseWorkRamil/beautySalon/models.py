from django.db import models
from django.contrib.auth.models import User

# Классы моделей

class Specialization(models.Model):
    ''' Модель для описания в базе данных таблицы со специализациями,
     к которым будут относиться процедуры и мастера '''
    name = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return f'Специализация {self.name}'

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Master(models.Model):
    ''' Модель для описания в базе данных таблицы с информацией о мастерах '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name='Специализация')
    image = models.ImageField(upload_to=f'images/masters/{user}', verbose_name='Изображение')

    def __str__(self):
        return f'Мастер-{self.specialization.name}, {self.user.name}'

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастеры"



class Service(models.Model):
    ''' Модель для описания в базе данных таблицы оценок, выставленных мастерам пользователями '''
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Стоимость')
    image = models.ImageField(upload_to=f'images/services/{name}', verbose_name='Изображение')

    def __str__(self):
        return f'Процедура "{self.name}"'

    class Meta:
        verbose_name = "Процедура"
        verbose_name_plural = "Процедуры"

class Appointment(models.Model):
    ''' Модель для описания в базе данных таблицы записей пользователей на ту или иную процедуру '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Процедура')
    date = models.DateField(null=False, auto_now=False, auto_now_add=False, verbose_name='Дата приема')
    time = models.TimeField(null=False, auto_now=False, auto_now_add=False, verbose_name="Время приема")

    def __str__(self):
            return f'Запись №{self.id} на {self.time} {self.date}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class MasterRating(models.Model):
    ''' Модель для описания в базе данных таблицы оценок, выставленных мастерам пользователями '''
    evaluating = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluating', verbose_name='Оценивающий')
    evaluated = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='evaluated', verbose_name='Оцениваемый')
    value = models.IntegerField(verbose_name='Оценка')

    class Meta:
        verbose_name = "Оценку"
        verbose_name_plural = "Оценки мастерам"


class Comment(models.Model):
    ''' Модель для описания в базе данных таблицы коментариев к профилям мастеров '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name='Мастер')
    text = models.TextField(verbose_name='Содержание')
    created_at = models.DateField(null=True, auto_now_add=True, verbose_name='Дата написания')

    def __str__(self):
            return f'Комментарий к профилю мастера {self.master.name}'

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к профилям авторов"


class Article(models.Model):
    ''' Модель для описания в базе данных таблицы новостных статей о косметике '''
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name='Содержание')
    image = models.ImageField(null=True, blank=True, upload_to='images/articles/%Y/%m/%d', verbose_name='Изображение')
    created_at = models.DateField(blank=True, null=True, auto_now_add=True, verbose_name='Дата написания')

    def __str__(self):
        return f'Статья №{self.id}'

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"
