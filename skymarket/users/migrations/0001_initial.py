# Generated by Django 3.2.6 on 2023-09-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='фамилия')),
                ('phone', models.CharField(blank=True, max_length=35, null=True, verbose_name='телефон')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('user', 'пользователь'), ('admin', 'администратор'), ('moderator', 'модератор')], default='user', max_length=10, verbose_name='роль пользователя')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='аватар')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]