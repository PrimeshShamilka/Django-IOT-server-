# Generated by Django 2.1.7 on 2019-05-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_auto_20190518_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
