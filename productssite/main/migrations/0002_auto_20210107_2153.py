# Generated by Django 3.1.5 on 2021-01-07 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='products',
        ),
        migrations.AlterField(
            model_name='sale',
            name='salerman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.salerman', verbose_name='Продавец'),
        ),
    ]
