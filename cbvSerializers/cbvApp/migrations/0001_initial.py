# Generated by Django 4.0.4 on 2022-04-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=52)),
                ('score', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
