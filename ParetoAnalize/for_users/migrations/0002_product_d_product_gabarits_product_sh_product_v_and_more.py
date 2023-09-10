# Generated by Django 4.2.4 on 2023-09-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='d',
            field=models.FloatField(default=0, verbose_name='Длина'),
        ),
        migrations.AddField(
            model_name='product',
            name='gabarits',
            field=models.CharField(default='', max_length=20, verbose_name='Артикул'),
        ),
        migrations.AddField(
            model_name='product',
            name='sh',
            field=models.FloatField(default=0, verbose_name='Ширина'),
        ),
        migrations.AddField(
            model_name='product',
            name='v',
            field=models.FloatField(default=0, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='product',
            name='weigh',
            field=models.FloatField(default=0, verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='sale',
            name='d',
            field=models.FloatField(default=0, verbose_name='Длина'),
        ),
        migrations.AddField(
            model_name='sale',
            name='gabarits',
            field=models.CharField(default='', max_length=20, verbose_name='Артикул'),
        ),
        migrations.AddField(
            model_name='sale',
            name='sh',
            field=models.FloatField(default=0, verbose_name='Ширина'),
        ),
        migrations.AddField(
            model_name='sale',
            name='v',
            field=models.FloatField(default=0, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='sale',
            name='weigh',
            field=models.FloatField(default=0, verbose_name='Вес'),
        ),
    ]
