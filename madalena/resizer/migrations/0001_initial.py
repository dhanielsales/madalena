# Generated by Django 3.0.5 on 2020-04-21 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funnel', '0002_entryimages_resized_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('image', models.ImageField(upload_to='result_images', verbose_name='Imagem de saída')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Adicionada em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificada em')),
                ('entry_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funnel.EntryImages', verbose_name='Imagem de entrada')),
            ],
            options={
                'verbose_name': 'Imagem de saída',
                'verbose_name_plural': 'Imagems de saída',
                'ordering': ['added_at'],
            },
        ),
    ]