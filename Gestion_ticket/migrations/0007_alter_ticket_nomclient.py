# Generated by Django 5.0.7 on 2024-08-22 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_ticket', '0006_alter_ticket_nomclient'),
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='nomClient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='authentification.client'),
        ),
    ]
