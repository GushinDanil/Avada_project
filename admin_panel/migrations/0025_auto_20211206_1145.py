# Generated by Django 3.2.8 on 2021-12-06 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0024_page_description2'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='seo_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='seo_block',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seoblock'),
        ),
    ]
