# Generated by Django 2.0.3 on 2018-03-22 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('open_humans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NokiaHealthMember',
            fields=[
                ('userid', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('deviceid', models.CharField(max_length=16)),
                ('oauth_token', models.CharField(max_length=256)),
                ('oauth_token_secret', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='open_humans.OpenHumansMember')),
            ],
        ),
    ]
