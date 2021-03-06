# Generated by Django 3.2.8 on 2021-12-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0027_alter_contact_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafeBarMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('weight', models.PositiveIntegerField(default=100, verbose_name='Вес(грамм)')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='Цена')),
            ],
            options={
                'db_table': 'cafe_bar_menu',
            },
        ),
    ]
