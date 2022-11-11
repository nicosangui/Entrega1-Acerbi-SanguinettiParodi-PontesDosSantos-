# Generated by Django 4.1.2 on 2022-11-07 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_delete_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]