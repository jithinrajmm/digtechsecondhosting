# Generated by Django 4.0.3 on 2022-04-25 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_options_alter_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'ordering': ('-created_at', '-updated_at')},
        ),
    ]
