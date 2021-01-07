from django.db import models
from django.contrib.postgres.validators import (MinValueValidator, MaxValueValidator)



class ProductGroup(models.Model):
    group_name = models.CharField('Название отдела', max_length = 70, unique=True)
    products_amount = models.IntegerField('Количество товаров в отделе', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Отдел продуктов"
        verbose_name_plural = "Отделы продуктов"

    def __str__(self):
        return self.group_name


class Products(models.Model):
    productGroup = models.ForeignKey(
        ProductGroup,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продукты'
    )
    title = models.CharField('Название', max_length = 60)
    brand = models.CharField('Фирма', max_length=50)
    description = models.TextField('Описание товара', blank=True)
    price = models.IntegerField('Цена, руб.', validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class Salerman(models.Model):
    salercode = models.IntegerField('Код продавца', validators=[MinValueValidator(1), MaxValueValidator(9999999)])
    salername = models.CharField('ФИО', max_length=250)
    cash = models.IntegerField('Заработная плата, руб.', validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

    def __str__(self):
        return self.salername


class Sale(models.Model):
    products = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продукт'
    )
    salecode = models.IntegerField('Код продажи', validators=[MinValueValidator(1), MaxValueValidator(9999999)], unique=True)
    salesumm = models.IntegerField('Сумма товара, руб.',validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return str(self.salecode)

class SaleCheck(models.Model):
    salerman = models.ForeignKey(
        Salerman,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продавец'
    )
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продажа'
    )
    salecheckcode = models.IntegerField('Код чека', validators=[MinValueValidator(1), MaxValueValidator(9999999)], unique=True)
    salechecksumm = models.IntegerField('Сумма чека, руб.',validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"

    def __str__(self):
        return str(self.salecheckcode)