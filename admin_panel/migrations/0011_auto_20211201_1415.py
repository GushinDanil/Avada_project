# Generated by Django 3.2.8 on 2021-12-01 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_auto_20211201_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='seo_block',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seoblock'),
        ),
        migrations.CreateModel(
            name='StockImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.stock')),
            ],
            options={
                'db_table': 'stock_imgs',
            },
        ),
    ]