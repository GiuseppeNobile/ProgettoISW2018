# Generated by Django 2.0.7 on 2018-07-25 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingApp', '0002_auto_20180725_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Albergatore'),
        ),
    ]