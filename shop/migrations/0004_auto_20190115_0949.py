# Generated by Django 2.1.3 on 2019-01-15 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190114_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='bannerimage',
            field=models.ImageField(upload_to='banner/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]