# Generated by Django 3.0.5 on 2020-04-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funnel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entryimages',
            name='resized_image',
            field=models.ImageField(blank=True, null=True, upload_to='resized_image', verbose_name='Imagem redimensionada'),
        ),
    ]
