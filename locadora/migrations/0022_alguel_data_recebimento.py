# Generated by Django 2.2.6 on 2019-11-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0021_auto_20191113_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='alguel',
            name='data_recebimento',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
