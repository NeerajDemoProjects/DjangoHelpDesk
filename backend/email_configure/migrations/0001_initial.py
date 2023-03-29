# Generated by Django 4.1.7 on 2023-03-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OutgoingEmailServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('email_password', models.CharField(max_length=100)),
                ('smtp_server', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
            ],
        ),
    ]
