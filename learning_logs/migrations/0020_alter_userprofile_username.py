# Generated by Django 4.2.4 on 2023-09-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0019_alter_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]
