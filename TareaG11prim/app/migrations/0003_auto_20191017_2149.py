# Generated by Django 2.2 on 2019-10-17 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191017_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='foto',
            field=models.ImageField(upload_to='app/img/'),
        ),
    ]
