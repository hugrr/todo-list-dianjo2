# Generated by Django 2.2 on 2019-08-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_todo_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_event',
            field=models.CharField(default='', max_length=200),
        ),
    ]
