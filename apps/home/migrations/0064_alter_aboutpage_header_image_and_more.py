# Generated by Django 4.1.2 on 2022-11-20 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_employee_image'),
        ('home', '0063_alter_aboutpage_header_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.accessibleimage'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='reverse_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.accessibleimage'),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='reverse_header',
            field=models.BooleanField(default=False),
        ),
    ]
