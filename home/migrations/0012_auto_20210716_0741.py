# Generated by Django 3.0.4 on 2021-07-16 01:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210715_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ratings',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]