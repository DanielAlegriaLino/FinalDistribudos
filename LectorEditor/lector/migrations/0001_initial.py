# Generated by Django 5.0 on 2023-12-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('date', models.DateField()),
                ('user', models.CharField(max_length=255)),
            ],
        ),
    ]
