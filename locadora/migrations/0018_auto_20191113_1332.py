# Generated by Django 2.2.6 on 2019-11-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0017_auto_20191113_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='status',
            field=models.CharField(choices=[('D', 'DISPONIVEL'), ('I', 'INDISPONIVEL')], max_length=14),
        ),
    ]