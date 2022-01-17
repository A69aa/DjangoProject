# Generated by Django 4.0.1 on 2022-01-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_book_create_date_remove_book_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Detective', 'Detective'), ('Comedy', 'Comedy'), ('History', 'History'), ('Fantasy', 'Fantasy'), ('SelfEducation', 'SelfEducation'), ('Classic', 'Classic')], max_length=100, null=True),
        ),
    ]
