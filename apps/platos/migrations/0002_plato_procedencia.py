# Generated by Django 4.1.3 on 2022-12-19 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='procedencia',
            field=models.CharField(default='sin origen', max_length=15),
        ),
    ]
