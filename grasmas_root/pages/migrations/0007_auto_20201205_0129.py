# Generated by Django 3.1.3 on 2020-12-05 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_gift_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='giver',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='gift',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]