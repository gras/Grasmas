# Generated by Django 3.1.3 on 2020-12-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20201205_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='gift',
            name='image',
            field=models.CharField(max_length=12),
        ),
    ]