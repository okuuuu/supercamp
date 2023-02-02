# Generated by Django 4.1 on 2023-02-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sufis', '0003_bookinlibrary_alter_order_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinlibrary',
            name='picture',
        ),
        migrations.AddField(
            model_name='bookinlibrary',
            name='is_public',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinlibrary',
            name='picture_link',
            field=models.CharField(default=None, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookinlibrary',
            name='status',
            field=models.CharField(default=False, max_length=512),
            preserve_default=False,
        ),
    ]
