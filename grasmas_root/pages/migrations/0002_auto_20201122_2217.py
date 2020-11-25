# Generated by Django 3.1.3 on 2020-11-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giver', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=12)),
                ('desc', models.CharField(max_length=12)),
                ('long', models.CharField(max_length=120)),
                ('recvr', models.CharField(blank=True, max_length=12)),
                ('authr', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]