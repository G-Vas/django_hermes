# Generated by Django 3.2.3 on 2021-05-25 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_productfeatures_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='features',
        ),
    ]
