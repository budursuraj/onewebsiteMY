# Generated by Django 5.0.1 on 2024-02-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=20)),
                ('ln', models.CharField(max_length=15)),
                ('ed', models.CharField(max_length=50)),
                ('cm', models.TextField()),
            ],
        ),
    ]