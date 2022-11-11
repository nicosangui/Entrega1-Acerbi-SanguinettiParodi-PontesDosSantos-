# Generated by Django 4.1.2 on 2022-11-10 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0009_alter_chat_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='nombre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
