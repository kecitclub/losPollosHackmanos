# Generated by Django 5.1.3 on 2025-01-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_login2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='reviews',
            new_name='rating',
        ),
        migrations.AddField(
            model_name='profile',
            name='worker_type',
            field=models.CharField(default='NULL', max_length=40),
        ),
    ]
