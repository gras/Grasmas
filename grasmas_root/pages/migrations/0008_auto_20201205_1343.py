# Generated by Django 3.1.3 on 2020-12-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20201205_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]