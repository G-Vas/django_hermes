# Generated by Django 3.2.3 on 2021-05-31 21:21

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_callrequests_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callrequests',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон'),
        ),
    ]