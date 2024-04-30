# Generated by Django 4.2.10 on 2024-04-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('no', models.IntegerField()),
                ('role', models.CharField(max_length=40)),
                ('salary', models.FloatField()),
                ('location', models.CharField(max_length=40)),
            ],
        ),
    ]