# Generated by Django 4.0.3 on 2022-04-18 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_alter_coupon_valid_from_alter_coupon_valid_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(),
        ),
    ]
