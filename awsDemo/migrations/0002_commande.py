# Generated by Django 3.1 on 2021-06-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awsDemo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Nom de l'article")),
                ('title', models.CharField(max_length=254, verbose_name='Titre')),
            ],
            options={
                'verbose_name': 'Commande',
                'verbose_name_plural': 'Commandes',
            },
        ),
    ]