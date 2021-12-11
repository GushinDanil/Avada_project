# Generated by Django 3.2.8 on 2021-12-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0020_auto_20211205_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='card_img',
            field=models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка карточки'),
        ),
        migrations.AddField(
            model_name='stock',
            name='card_img',
            field=models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка карточки'),
        ),
    ]