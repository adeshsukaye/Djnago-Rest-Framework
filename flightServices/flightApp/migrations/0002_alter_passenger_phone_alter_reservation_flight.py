# Generated by Django 4.0.4 on 2022-04-16 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightApp.flight'),
        ),
    ]
