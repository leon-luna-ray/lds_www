# Generated by Django 4.1.2 on 2022-11-13 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_aboutpage_reverse_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='reverse_header',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
