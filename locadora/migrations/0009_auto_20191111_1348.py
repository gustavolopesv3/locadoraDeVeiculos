# Generated by Django 2.2.6 on 2019-11-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0008_auto_20191111_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alguel',
            name='data_retorno',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='alguel',
            name='valor',
            field=models.CharField(max_length=9),
        ),
    ]
