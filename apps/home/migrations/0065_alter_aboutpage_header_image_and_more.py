# Generated by Django 4.1.2 on 2022-11-22 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_employee_image'),
        ('home', '0064_alter_aboutpage_header_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.accessibleimage'),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.accessibleimage'),
        ),
    ]