# Generated by Django 3.1.3 on 2020-11-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201123_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='color',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
