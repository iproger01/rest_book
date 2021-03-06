# Generated by Django 3.2.7 on 2021-11-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatistData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_books', models.IntegerField(verbose_name='Кол-во книг')),
                ('save_date', models.DateField(auto_now_add=True, verbose_name='День сохранения')),
                ('save_books_name', models.CharField(max_length=1500, verbose_name='Книги, которые добавили в этот день')),
            ],
            options={
                'verbose_name': 'статистику за день',
                'verbose_name_plural': 'статистика за день',
            },
        ),
    ]
