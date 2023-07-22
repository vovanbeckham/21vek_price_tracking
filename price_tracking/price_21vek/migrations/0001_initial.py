# Generated by Django 4.1.7 on 2023-04-06 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название каталога')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('url_categories', models.URLField()),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('catalogs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='price_21vek.catalog')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url_img', models.URLField(max_length=250)),
                ('url_product', models.URLField(max_length=250)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='price_21vek.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='price_21vek.product')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
                'ordering': ('price',),
            },
        ),
    ]
