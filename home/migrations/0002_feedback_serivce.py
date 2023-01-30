# Generated by Django 4.1.5 on 2023-01-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('post', models.CharField(max_length=300)),
                ('image', models.TextField()),
                ('comment', models.TextField()),
                ('address1', models.CharField(max_length=400)),
                ('address2', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=500)),
                ('time', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Serivce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.CharField(max_length=400)),
                ('description', models.TextField()),
            ],
        ),
    ]
