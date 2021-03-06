# Generated by Django 3.1.5 on 2021-01-07 18:59

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210107_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.products', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='salerman',
            field=models.IntegerField(blank=True, null=True, verbose_name=main.models.Salerman),
        ),
    ]
