# Generated by Django 4.1.2 on 2022-11-13 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_employee_image'),
        ('home', '0043_alter_aboutpage_content_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.accessibleimage'),
        ),
    ]
