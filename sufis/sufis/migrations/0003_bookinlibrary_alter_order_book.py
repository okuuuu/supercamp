# Generated by Django 4.1 on 2023-02-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sufis', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInLiBrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='./')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sufis.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sufis.user')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sufis.bookinlibrary'),
        ),
    ]
