# Generated by Django 3.2.25 on 2024-05-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_producto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(upload_to='Ferremas/core/static/img/'),
        ),
    ]
