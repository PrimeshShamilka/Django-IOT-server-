# Generated by Django 2.1.7 on 2019-05-26 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('values', models.FileField(blank=True, null=True, upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('local_ip', models.CharField(max_length=100, null=True)),
                ('mac_address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='devices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.devices'),
        ),
    ]
