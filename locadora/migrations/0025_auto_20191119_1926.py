# Generated by Django 2.2.6 on 2019-11-20 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0024_auto_20191118_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alguel',
            name='data_recebimento',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
