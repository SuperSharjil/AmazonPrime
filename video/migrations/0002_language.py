# Generated by Django 3.0.5 on 2020-07-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.IntegerField(primary_key=True, serialize=False)),
                ('language_name', models.CharField(max_length=100)),
            ],
        ),
    ]
