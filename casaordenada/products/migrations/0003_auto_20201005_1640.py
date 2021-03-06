# Generated by Django 3.0.8 on 2020-10-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201005_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country_id',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer_id',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='number_id',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
