# Generated by Django 3.2.8 on 2021-11-26 18:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('banner', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('logo', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'cinema',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('address', models.TextField()),
                ('coordinate', models.CharField(max_length=200)),
                ('logo', models.URLField()),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'editors',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('card_img', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка карточки')),
                ('released', models.DateField(verbose_name='Дата выхода')),
                ('trailer_link', models.URLField(max_length=100, verbose_name='Ссылка на трейлер')),
                ('banner', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/', verbose_name='Баннер')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('budget', models.CharField(max_length=15, verbose_name='Бюджет')),
                ('legal_age', models.PositiveIntegerField(verbose_name='Мин Возраст')),
                ('duration', models.CharField(max_length=15, verbose_name='Длительность')),
                ('countries', models.ManyToManyField(to='admin_panel.Country', verbose_name='Страны')),
                ('editors', models.ManyToManyField(to='admin_panel.Editor', verbose_name='Режисёры')),
            ],
            options={
                'db_table': 'films',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('banner', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(default='')),
                ('num_tickets', models.PositiveSmallIntegerField()),
                ('scheme', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('creation_date', models.DateField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.cinema')),
            ],
            options={
                'db_table': 'halls',
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, unique=True)),
                ('number2', models.CharField(max_length=100, unique=True)),
                ('seo_block', models.TextField()),
            ],
            options={
                'db_table': 'main_page',
            },
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'operators',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('banner', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('created', models.DateField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.cinema')),
            ],
            options={
                'db_table': 'pages',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'producers',
            },
        ),
        migrations.CreateModel(
            name='ScriptWriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'scriptwriters',
            },
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(verbose_name='%H:%M')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.film')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.hall')),
            ],
            options={
                'db_table': 'seances',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.TextField(default='', max_length=50)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateTimeField(default=datetime.date(2021, 11, 26))),
                ('video_link', models.URLField()),
                ('banner', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'db_table': 'stocks',
            },
        ),
        migrations.CreateModel(
            name='TechnologyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'technology_type',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('nickname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('sex', models.BooleanField()),
                ('phone_number', models.TextField()),
                ('birthday', models.DateField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField()),
                ('row', models.PositiveSmallIntegerField()),
                ('seat', models.PositiveSmallIntegerField()),
                ('seance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seance')),
            ],
            options={
                'db_table': 'tickets',
            },
        ),
        migrations.AddField(
            model_name='seance',
            name='tech_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.technologytype'),
        ),
        migrations.CreateModel(
            name='PageImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.page')),
            ],
            options={
                'db_table': 'pages_imgs',
            },
        ),
        migrations.CreateModel(
            name='HallImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.hall')),
            ],
            options={
                'db_table': 'halls_imgs',
            },
        ),
        migrations.CreateModel(
            name='FilmImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.film')),
            ],
            options={
                'db_table': 'film_imgs',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(to='admin_panel.Genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='film',
            name='operators',
            field=models.ManyToManyField(to='admin_panel.Operator', verbose_name='Операторы'),
        ),
        migrations.AddField(
            model_name='film',
            name='producers',
            field=models.ManyToManyField(to='admin_panel.Producer', verbose_name='Продюсеры'),
        ),
        migrations.AddField(
            model_name='film',
            name='scriptwriters',
            field=models.ManyToManyField(to='admin_panel.ScriptWriter', verbose_name='Сценаристы'),
        ),
        migrations.AddField(
            model_name='film',
            name='technology_types',
            field=models.ManyToManyField(to='admin_panel.TechnologyType', verbose_name='Форматы'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.user')),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='CinemaImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, unique=True, upload_to='photos/%Y/%m/%d/')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.cinema')),
            ],
            options={
                'db_table': 'cinema_imgs',
            },
        ),
        migrations.AddField(
            model_name='cinema',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.contact'),
        ),
    ]