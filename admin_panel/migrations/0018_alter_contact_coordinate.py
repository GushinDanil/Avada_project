# Generated by Django 3.2.8 on 2021-12-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0017_auto_20211205_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='coordinate',
            field=models.TextField(max_length=10000),
        ),
    ]
