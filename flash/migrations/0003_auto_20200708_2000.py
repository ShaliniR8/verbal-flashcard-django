# Generated by Django 3.0.8 on 2020-07-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0002_auto_20200708_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='example1',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='example2',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='example3',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
