# Generated by Django 3.0.5 on 2020-07-31 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_language'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
