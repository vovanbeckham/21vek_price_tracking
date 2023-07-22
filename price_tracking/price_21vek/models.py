from django.db import models

class Catalog(models.Model):
    name = models.CharField('Название каталога', max_length=200)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}({self.pk})'


class Category(models.Model):
    name = models.CharField('Название категории', max_length=255)
    url_categories = models.URLField(max_length=200)
    catalogs = models.ForeignKey('Catalog', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}({self.pk})'




class Product(models.Model):
    categories = models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    url_img = models.URLField(max_length=250)
    url_product = models.URLField(max_length=250)
    time_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}({self.pk})'


class Prices(models.Model):
    products = models.ForeignKey('Product', on_delete=models.PROTECT)
    price = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ('price',)

    def __str__(self):
        return f'{self.price}({self.pk})'
