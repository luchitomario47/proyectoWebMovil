# Generated by Django 5.1 on 2024-08-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='detalle',
            field=models.TextField(default='detalle', max_length=100),
            preserve_default=False,
        ),
    ]
