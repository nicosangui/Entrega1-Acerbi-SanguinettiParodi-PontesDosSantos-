# Generated by Django 4.1.2 on 2022-10-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('lugar_de_nacimiento', models.CharField(max_length=20)),
                ('fecha_de_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('ocupacion', models.CharField(max_length=20)),
            ],
        ),
    ]
