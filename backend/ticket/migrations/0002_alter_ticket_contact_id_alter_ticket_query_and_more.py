# Generated by Django 4.1.7 on 2023-03-25 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='contact_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.contact'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='query',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='state_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact.status'),
        ),
    ]
