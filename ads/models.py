from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'


class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    username = models.CharField(max_length=20, verbose_name='Ник')
    password = models.CharField(max_length=128, verbose_name='пароль')
    role = models.CharField(max_length=9, default="member", verbose_name='Роль')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username


class Ad(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Стоимость')
    description = models.TextField(verbose_name='Описание')
    is_publisher = models.BooleanField(verbose_name='Опубликована')
    image = models.ImageField(upload_to="ads/", null=True, blank=True, verbose_name='Фото')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return f'{self.name} - {self.price}'
