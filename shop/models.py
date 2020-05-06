from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=70, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=70, verbose_name="Наименование")
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name="В наличии")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField(verbose_name="Цена")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    total_sum = models.PositiveIntegerField(verbose_name="Сумма", blank=True, null=True)

    class Meta():
        ordering = ["-price", "name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        unique_together = ["category", "name", "price"]

    def save(self, *args, **kwargs):
        self.total_sum = self.price * self.quantity

        super(Good, self).save(*args, **kwargs)



    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + "Нет в наличии"
        return s



