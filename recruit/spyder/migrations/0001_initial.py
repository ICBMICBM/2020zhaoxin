# Generated by Django 2.2.7 on 2020-10-13 16:22

from django.db import migrations, models
import spyder.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('flag', models.CharField(default=spyder.models.make_flag, max_length=12)),
            ],
        ),
    ]
