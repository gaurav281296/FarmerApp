# Generated by Django 2.2.1 on 2019-05-16 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('PricePerSIunit', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
