# Generated by Django 3.2.8 on 2021-12-05 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0012_news_newsimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimg',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.news'),
        ),
    ]
