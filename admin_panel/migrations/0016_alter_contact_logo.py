# Generated by Django 3.2.8 on 2021-12-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0015_auto_20211205_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='logo',
            field=models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]