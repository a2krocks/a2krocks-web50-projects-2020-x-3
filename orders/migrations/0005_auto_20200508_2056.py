# Generated by Django 3.0.6 on 2020-05-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart_total_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_item',
        ),
        migrations.AddField(
            model_name='cart',
            name='pasta_quatity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='salad_quatity',
            field=models.IntegerField(default=0),
        ),
    ]
