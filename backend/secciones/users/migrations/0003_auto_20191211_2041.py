# Generated by Django 2.2 on 2019-12-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191211_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='phone',
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.IntegerField(unique=True),
        ),
    ]