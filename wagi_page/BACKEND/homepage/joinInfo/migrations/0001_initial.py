# Generated by Django 4.2.3 on 2024-01-02 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JoinInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15)),
                ('user_number', models.IntegerField()),
                ('user_major', models.CharField(max_length=30)),
                ('user_phone_number', models.IntegerField()),
            ],
        ),
    ]