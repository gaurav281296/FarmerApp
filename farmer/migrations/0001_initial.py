# Generated by Django 2.2.1 on 2019-05-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Language', models.CharField(max_length=20)),
            ],
        ),
    ]
