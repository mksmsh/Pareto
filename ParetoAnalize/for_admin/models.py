from django.db import models


class MarketPlace(models.Model):
    nameMP = models.CharField(max_length=20, verbose_name='Название МП', unique=True)

    def __str__(self):
        return self.nameMP

    class Meta:
        verbose_name = "Маркетплейс"
        verbose_name_plural = "Маркетплейсы"


class ModelWork(models.Model):
    nameMW = models.CharField(max_length=10, verbose_name='Название модели', unique=True)
    mp = models.ForeignKey(MarketPlace, on_delete=models.CASCADE, verbose_name='Доступе для МП', to_field='nameMP')

    def __str__(self):
        return self.nameMW

    class Meta:
        verbose_name = "Модель продаж"
        verbose_name_plural = "Модели продаж"


class MethodofExport(models.Model):
    nameME = models.CharField(max_length=20, verbose_name='Метод отгрузки', unique=True)
    cost = models.FloatField(verbose_name='Стоимость отгрузки')
    mp = models.ForeignKey(MarketPlace, on_delete=models.CASCADE, verbose_name='Доступно для МП', to_field='nameMP', default='МП')
    mw = models.ForeignKey(ModelWork, on_delete=models.CASCADE, verbose_name='Доступно для модели', to_field='nameMW')

    def __str__(self):
        return self.nameME

    class Meta:
        verbose_name = "Метод отгрузки"
        verbose_name_plural = "Методы для отгрузки"


class TariffTranslate(models.Model):
    nameTT = models.CharField(max_length=20, verbose_name='Частота выплат', unique=True)
    cost = models.FloatField(verbose_name='Стоимость')
    cost_tt_client = models.FloatField(verbose_name='Стоимость за прием платежей покупателей', default=0.12)
    mp = models.ForeignKey(MarketPlace, on_delete=models.CASCADE, verbose_name='Доступно для МП', to_field='nameMP')

    def __str__(self):
        return self.nameTT

    class Meta:
        verbose_name = "Тариф перевода денег"
        verbose_name_plural = "Тарифы перевода денег"


class Category (models.Model):
    nameCT = models.CharField(max_length=20, verbose_name='Имя', unique=True)
    cost = models.FloatField(verbose_name='Комиссия')
    mp = models.ForeignKey(MarketPlace, on_delete=models.CASCADE, verbose_name='Доступно для МП', to_field='nameMP')

    def __str__(self):
        return self.nameCT

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class CategoryYM(models.Model):
    name_parents = models.CharField(max_length=10, verbose_name='Родительская')
    name_dote = models.CharField(max_length=50, verbose_name='Дочерняя')
    name_full = models.CharField(max_length=60, verbose_name='Полное имя категории')

    cost_fby = models.FloatField(verbose_name='Комиссия для модели FBY')
    cost_fbs = models.FloatField(verbose_name='Комиссия для модели FSY', null=True)

    def save(self, *args, **kwargs):
        if self.name_dote:
            self.name_dote = self.name_dote.replace('-', '/')

            part = self.name_dote.split('/')
            if part[0] == self.name_parents:
                self.name_full = self.name_dote
            else:
                self.name_full = self.name_parents + '/' + self.name_dote

        if self.cost_fbs == None:
            self.cost_fbs = self.cost_fby

        super(CategoryYM, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_full

    class Meta:
        verbose_name = "Категория Яндекс.Маркет"
        verbose_name_plural = "Категории Яндекс.Маркет"


class CategoryOZ(models.Model):
    name_category = models.CharField(max_length=60, verbose_name='Имя категории')

    cost_fbo = models.FloatField(verbose_name='Комиссия для модели FBO')
    cost_fbs = models.FloatField(verbose_name='Комиссия для модели FBS')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория Озон"
        verbose_name_plural = "Категории Озон"


class CategorySBR(models.Model):
    name_category = models.CharField(max_length=60, verbose_name='Имя категории')

    cost_fbo = models.FloatField(verbose_name='Комиссия для модели FBO')
    cost_fbs = models.FloatField(verbose_name='Комиссия для модели FBS')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория СберМегаМаркет"
        verbose_name_plural = "Категории СберМегаМаркет"


#class EnotherTariffYM (models.Model):
