# Generated by Django 2.2.6 on 2019-11-18 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0023_auto_20191118_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alguel',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locadora.Cliente'),
        ),
        migrations.AlterField(
            model_name='alguel',
            name='data_locacao',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='alguel',
            name='data_retorno',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='alguel',
            name='observacao',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='alguel',
            name='valor',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='alguel',
            name='veiculo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locadora.Veiculo'),
        ),
    ]