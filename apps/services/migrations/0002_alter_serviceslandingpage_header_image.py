# Generated by Django 4.1.2 on 2022-11-13 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_employee_image'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceslandingpage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.accessibleimage'),
        ),
    ]
