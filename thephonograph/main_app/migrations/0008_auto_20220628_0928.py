# Generated by Django 3.1.3 on 2022-06-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20220627_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='artists',
        ),
        migrations.AddField(
            model_name='artist',
            name='records',
            field=models.ManyToManyField(to='main_app.Record'),
        ),
    ]
