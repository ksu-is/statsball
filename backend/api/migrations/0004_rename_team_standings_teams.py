# Generated by Django 5.1.2 on 2024-10-18 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_teams_standings_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='standings',
            old_name='team',
            new_name='teams',
        ),
    ]
