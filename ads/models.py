from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    author = models.CharField(max_length=50, verbose_name='Автор')
    price = models.IntegerField(verbose_name='Стоимость')
    description = models.TextField(verbose_name='Описание')
    address = models.TextField(verbose_name='Адрес')
    is_publisher = models.BooleanField(verbose_name='Опубликована')

    def __str__(self):
        return f'{self.name} - {self.price}'


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return f'{self.name}'