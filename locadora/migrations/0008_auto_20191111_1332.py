# Generated by Django 2.2.6 on 2019-11-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0007_auto_20191111_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
