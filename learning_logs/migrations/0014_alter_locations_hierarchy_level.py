# Generated by Django 4.2.4 on 2023-09-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0013_locations_users_alter_locations_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='hierarchy_level',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
