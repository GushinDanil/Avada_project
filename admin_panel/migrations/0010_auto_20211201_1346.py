# Generated by Django 3.2.8 on 2021-12-01 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_alter_hall_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='created_at',
        ),
        migrations.AddField(
            model_name='stock',
            name='creation_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='turn_on',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hall',
            name='cinema',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.cinema'),
        ),
    ]
