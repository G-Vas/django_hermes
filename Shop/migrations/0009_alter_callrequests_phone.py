# Generated by Django 3.2.3 on 2021-05-31 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_alter_callrequests_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrequests',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
