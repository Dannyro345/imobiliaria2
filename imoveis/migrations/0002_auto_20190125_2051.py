# Generated by Django 2.1.2 on 2019-01-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.AlterField(
            model_name='imovel',
            name='valor',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
