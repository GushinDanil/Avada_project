# Generated by Django 3.2.8 on 2021-12-06 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0025_auto_20211206_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cinema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.cinema'),
        ),
    ]