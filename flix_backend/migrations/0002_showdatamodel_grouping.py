# Generated by Django 5.0.6 on 2024-08-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flix_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='showdatamodel',
            name='grouping',
            field=models.CharField(default='No Group', max_length=100),
        ),
    ]