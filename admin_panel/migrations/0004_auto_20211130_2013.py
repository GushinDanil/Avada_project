# Generated by Django 3.2.8 on 2021-11-30 20:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_auto_20211126_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=150)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
            ],
            options={
                'db_table': 'seo_block',
            },
        ),
        migrations.AlterField(
            model_name='filmimg',
            name='img',
            field=models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='stock',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2021, 11, 30)),
        ),
        migrations.AddField(
            model_name='film',
            name='seo_block',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seoblock'),
        ),
    ]