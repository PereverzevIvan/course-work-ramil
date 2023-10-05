from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.safestring import mark_safe


# Классы моделей
class Specialization(models.Model):
    ''' Модель для описания в базе данных таблицы со специализациями,
     к которым будут относиться процедуры и мастера '''
    name = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Master(models.Model):
    ''' Модель для описания в базе данных таблицы с информацией о мастерах '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(upload_to=f'images/masters/', verbose_name='Изображение')
    specialization = models.ManyToManyField(Specialization, verbose_name='Специализации')

    def __str__(self):
        return f'Мастер-{self.specialization.name}, {self.user.username}'

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастеры"



class Service(models.Model):
    ''' Модель для описания в базе данных таблицы оценок, выставленных мастерам пользователями '''
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Стоимость')
    duration = models.IntegerField(null=False, blank=False, verbose_name='Длительность, мин')
    specialization = models.ForeignKey(Specialization, null=False, blank=False, on_delete=models.PROTECT, verbose_name='Сепциализация')

    def __str__(self):
        return f'"{self.name}"'

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


# Классы админки
class ServiceInlines(admin.TabularInline):
    model = Service
    fields = ['name', 'duration', 'price']

class CommentInlines(admin.TabularInline):
    model = Comment
    fields = ['author', 'text']


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    inlines = [ServiceInlines]


class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_image')
    list_display_links = ('id', 'user')
    search_fields = ['user__username', 'specialization']
    filter_horizontal = ['specialization']
    list_filter = ['specialization']

    inlines = [CommentInlines]

    def get_image(self, object):
        return mark_safe(f'<img src="/static/{object.image}" width=120>')
    
    get_image.short_description = 'Изображение'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'price', 'specialization')
    list_display_links = ('id', 'name')
    list_filter = ['specialization']
    search_fields = ['name', 'specialization']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'user', 'master', 'service')
    list_display_links = ('id', 'date', 'time')
    list_filter = ['service']
    search_fields = ['user__username', 'master__username']
    date_hierarchy = "date"


class MasterRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_info', 'value')
    list_display_links = ('id', 'get_info')
    search_fields = ['evaluating__username', 'evaluated__username']
    list_filter = ['value']

    def get_info(self, object):
        return f'Пользователь {object.evaluating.username} оценил пользователя {object.evaluated.username}'
    
    get_info.short_description = 'Информация'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'master', 'created_at')
    list_display_links = ('id', 'author')
    search_fields = ['author__username', 'master__username']
    readonly_fields = ['author', 'master', 'text', 'created_at']
    date_hierarchy = "created_at"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'get_image')
    list_display_links = ('id', 'title')
    search_fields = ['title']
    readonly_fields = ['created_at']
    list_filter = ['created_at']
    date_hierarchy = "created_at"

    def get_image(self, object):
        return mark_safe(f'<img src="/static/{object.image}" width=70>')
    
    get_image.short_description = 'Изображение'

