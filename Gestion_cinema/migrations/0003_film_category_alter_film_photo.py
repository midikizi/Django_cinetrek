# Generated by Django 5.0.7 on 2024-08-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_cinema', '0002_remove_film_category_alter_salle_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='category',
            field=models.ManyToManyField(to='Gestion_cinema.categorie', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='film',
            name='photo',
            field=models.ImageField(null=True, upload_to='films/'),
        ),
    ]
