# Generated by Django 4.2.7 on 2023-12-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
