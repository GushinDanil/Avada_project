# Generated by Django 3.2.8 on 2021-12-01 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_auto_20211201_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='seo_block',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seoblock'),
        ),
    ]
