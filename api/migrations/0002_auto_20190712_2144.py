# Generated by Django 2.2 on 2019-07-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=200)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]