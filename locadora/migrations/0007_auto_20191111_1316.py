# Generated by Django 2.2.6 on 2019-11-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0006_auto_20191111_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.CharField(max_length=15),
        ),
    ]
