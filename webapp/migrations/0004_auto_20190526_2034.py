# Generated by Django 2.1.7 on 2019-05-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_data_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]