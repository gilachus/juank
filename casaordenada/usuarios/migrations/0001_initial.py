# Generated by Django 3.0.8 on 2020-10-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_id', models.CharField(max_length=50)),
                ('tipo_documento', models.CharField(default='cédula', max_length=50)),
            ],
        ),
    ]
