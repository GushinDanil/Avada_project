# Generated by Django 3.2.8 on 2021-12-05 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0011_auto_20211201_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.stock')),
            ],
            options={
                'db_table': 'news_imgs',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.TextField(default='', max_length=50)),
                ('description', models.TextField(default='')),
                ('creation_date', models.DateField(auto_now_add=True, null=True)),
                ('turn_on', models.BooleanField(default=False)),
                ('video_link', models.URLField()),
                ('banner', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('seo_block', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seoblock')),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
