# Generated by Django 4.1.2 on 2022-11-22 04:39

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_employee_image'),
        ('services', '0023_remove_serviceslandingpage_header_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.accessibleimage'),
        ),
        migrations.AddField(
            model_name='gallerypage',
            name='reverse_header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='serviceslandingpage',
            name='header_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.accessibleimage'),
        ),
        migrations.AddField(
            model_name='serviceslandingpage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='serviceslandingpage',
            name='reverse_header',
            field=models.BooleanField(default=False),
        ),
    ]