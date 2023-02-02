# Generated by Django 4.1 on 2023-02-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sufis', '0005_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='en', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='no', max_length=512),
            preserve_default=False,
        ),
    ]
