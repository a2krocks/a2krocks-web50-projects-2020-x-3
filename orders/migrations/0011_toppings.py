# Generated by Django 3.0.6 on 2020-05-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_cart_pizza_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
    ]
