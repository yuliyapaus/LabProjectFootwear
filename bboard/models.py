from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Товар")
    content = models.TextField(blank=True, null=True, verbose_name="Описание")
    price = models.FloatField(blank=True, null=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    rubric = models.ForeignKey(
        'Rubric',
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Рубрика'
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-published']


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
