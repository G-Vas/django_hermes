# Generated by Django 3.2.3 on 2021-05-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_callrequests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrequests',
            name='phone',
            field=models.IntegerField(unique=True, verbose_name='Телефон'),
        ),
    ]
