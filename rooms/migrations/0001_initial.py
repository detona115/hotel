# Generated by Django 4.0.2 on 2022-02-07 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Numero')),
                ('size', models.IntegerField(verbose_name='Taille')),
                ('nb_bed', models.IntegerField(verbose_name='Nombre de lit')),
                ('type_of_bed', models.CharField(max_length=250, verbose_name='Type de lit')),
                ('frigo_bar', models.BooleanField(default=False, verbose_name='Frigo Bar')),
            ],
        ),
    ]
