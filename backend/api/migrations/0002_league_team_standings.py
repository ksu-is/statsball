# Generated by Django 5.1.2 on 2024-10-18 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('emblem', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('crest', models.URLField()),
                ('position', models.IntegerField()),
                ('playedGames', models.IntegerField()),
                ('won', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('points', models.IntegerField()),
                ('goalDifference', models.IntegerField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='api.league')),
            ],
        ),
        migrations.CreateModel(
            name='Standings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standings', to='api.league')),
                ('teams', models.ManyToManyField(related_name='standings', to='api.team')),
            ],
        ),
    ]
