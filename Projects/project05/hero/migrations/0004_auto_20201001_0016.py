# Generated by Django 3.1.1 on 2020-10-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_superhero_heroid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='heroId',
        ),
        migrations.AlterField(
            model_name='superhero',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]