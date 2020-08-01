# Generated by Django 3.0.5 on 2020-07-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.IntegerField(primary_key=True, serialize=False)),
                ('video_title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
