from django.contrib.auth.models import User
from django.db import models
from for_admin.models import MarketPlace, ModelWork, MethodofExport, TariffTranslate


class Shop(models.Model):
    nameSH = models.CharField(max_length=20, verbose_name='Название', unique=True)

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')

    mp = models.ForeignKey(MarketPlace, on_delete=models.CASCADE, verbose_name='Маркетплейс', to_field='nameMP')
    md = models.ForeignKey(ModelWork, on_delete=models.CASCADE, verbose_name='Модель работы', to_field='nameMW')
    moe = models.ForeignKey(MethodofExport, on_delete=models.CASCADE, verbose_name='Метод отгрузки', to_field='nameME')
    tt = models.ForeignKey(TariffTranslate, on_delete=models.CASCADE, verbose_name='Тариф перевода денег', to_field='nameTT')


    def __str__(self):
        return self.nameSH

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"


class Product(models.Model):
    sku = models.CharField(max_length=20, verbose_name='Уникальный номер на площадке')
    nameP = models.CharField(max_length=20, verbose_name='Название')
    category = models.CharField(max_length=50, verbose_name='Категория')
    article = models.CharField(max_length=20, verbose_name='Артикул')
    price = models.FloatField(verbose_name='Цена продажи', default=0, null=True)
    profit = models.FloatField(verbose_name='Прибыль', default=0, null=True)

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин', to_field='nameSH')

    def __str__(self):
        return self.nameP

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Sale(models.Model):
    number_shop = models.CharField(max_length=20, verbose_name='Номер')
    sku_p = models.CharField(max_length=20, verbose_name='Уникальный номер на площадке')
    name_p = models.CharField(max_length=20, verbose_name='Название')
    count = models.IntegerField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Цена продажи', null=True)
    profit = models.FloatField(verbose_name='Прибыль',  null=True)
    category = models.CharField(max_length=50, verbose_name='Категория')

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин', to_field='nameSH')

    def __str__(self):
        return self.name_p

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"