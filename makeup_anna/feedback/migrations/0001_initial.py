# Generated by Django 3.2.18 on 2023-05-02 16:12

from django.db import migrations, models
import feedback.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите ваше имя.', max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(help_text='Введите номер телефона для связи.', max_length=20, verbose_name='Номер телефона')),
                ('message', models.TextField(help_text='Напишите здесь информацию\n         о которой необходимо знать мастеру.', max_length=200, verbose_name='Информация')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки изображения')),
            ],
        ),
        migrations.CreateModel(
            name='Сountdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, help_text='Введите дату и время окончания акции\n        в формате 2022-02-22 22:22:22.', null=True, validators=[feedback.validators.validate_datetime, feedback.validators.validate_not_past], verbose_name='Дата и время окончания акции')),
            ],
        ),
    ]
