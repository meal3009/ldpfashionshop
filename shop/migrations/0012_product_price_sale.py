# Generated by Django 2.1.3 on 2019-02-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20190213_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_sale',
            field=models.PositiveIntegerField(default='10', verbose_name='price (฿)'),
            preserve_default=False,
        ),
    ]
