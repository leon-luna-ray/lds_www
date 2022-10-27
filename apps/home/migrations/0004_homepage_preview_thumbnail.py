# Generated by Django 4.1.2 on 2022-10-27 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('home', '0003_homepage_banner_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='preview_thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.accessibleimage'),
        ),
    ]
