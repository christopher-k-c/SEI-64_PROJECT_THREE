# Generated by Django 3.1.3 on 2022-06-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('format', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('image', models.URLField(max_length=1000)),
            ],
        ),
    ]
