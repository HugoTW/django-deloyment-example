# Generated by Django 2.2.1 on 2019-08-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, unique=True)),
                ('firstName', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=128)),
            ],
        ),
    ]
