# Generated by Django 2.2.6 on 2019-11-13 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0018_auto_20191113_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='marca',
        ),
    ]
