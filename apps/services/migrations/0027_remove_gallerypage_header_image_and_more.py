# Generated by Django 4.1.2 on 2022-11-22 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_gallerypage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallerypage',
            name='header_image',
        ),
        migrations.RemoveField(
            model_name='gallerypage',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='gallerypage',
            name='preview_thumbnail',
        ),
        migrations.RemoveField(
            model_name='gallerypage',
            name='reverse_header',
        ),
    ]