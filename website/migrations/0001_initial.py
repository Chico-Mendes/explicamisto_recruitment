# Generated by Django 5.0.1 on 2024-01-15 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Testemunho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('year', models.CharField(max_length=5)),
                ('occupation', models.CharField(choices=[('Explicadore', 'Explicadore'), ('Explicador', 'Explicador'), ('Explicadora', 'Explicadora'), ('Explicande', 'Explicande'), ('Explicando', 'Explicando'), ('Explicanda', 'Explicanda')], default='Explicadore', max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.person')),
            ],
        ),
    ]
