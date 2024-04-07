# Generated by Django 5.0.4 on 2024-04-06 21:23

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0008_auto_20240406_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='flash.topic')),
                ('content', models.TextField()),
            ],
        )
    ]