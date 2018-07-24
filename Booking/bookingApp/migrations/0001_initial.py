# Generated by Django 2.0.7 on 2018-07-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albergatore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30)),
                ('numeroHotel', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomehotel', models.CharField(max_length=30)),
                ('deschotel', models.CharField(max_length=100)),
                ('cittahotel', models.CharField(max_length=30)),
                ('indhotel', models.CharField(max_length=30)),
                ('numStanze', models.IntegerField()),
                ('proprietario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Prenotazione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPrenotazione', models.IntegerField()),
                ('cliente', models.CharField(max_length=30)),
                ('stanza', models.IntegerField()),
                ('data', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Stanza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numStanza', models.IntegerField()),
                ('postiletto', models.IntegerField()),
                ('servizi', models.CharField(max_length=100)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotelDiAppartenenza', models.CharField(max_length=30)),
            ],
        ),
    ]
