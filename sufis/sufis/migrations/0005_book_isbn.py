# Generated by Django 4.1 on 2023-02-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sufis', '0004_remove_bookinlibrary_picture_bookinlibrary_is_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=False, max_length=512),
            preserve_default=False,
        ),
    ]