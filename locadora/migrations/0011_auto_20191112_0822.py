# Generated by Django 2.2.6 on 2019-11-12 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0010_modelo_marca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelo',
            old_name='marca',
            new_name='nome_marca',
        ),
    ]
