from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

class Bb(models.Model):
    KINDS = (
        (None, "Что будем с этим делать?"),
        ('b', 'Хочу! Куплю!'),
        ('s', 'Отдам в хорошие руки. За червонец'),
        ('c', 'Меняю на самовар'),
    )
    title = models.CharField(
        max_length=50,
        verbose_name="Товар",
        validators=[validators.RegexValidator(regex='^.{4,}$')],
        error_messages={'invalid':'Неверное название товара'}
    )
    content = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.FloatField(blank=True, null=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    rubric = models.ForeignKey(
        'Rubric',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Рубрика'
    )
    kind = models.CharField(
        max_length=1,
        choices=KINDS,
        verbose_name="Варианты использования",
        default='b',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-published']

    def title_and_price(self):
        if self.price:
            return '%s (%.2f)' %(self.title, self.price)
        else:
            return self.title
    title_and_price.short_description = 'Название и цена'

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите писание товара')
        if self.price and self.price < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значение цены')
        if errors:
            raise ValidationError(errors)


class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/bboard/%s" %self.pk
