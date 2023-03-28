# Generated by Django 4.1.7 on 2023-03-28 16:08

from django.db import migrations
import ticket.models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_ticket_contact_id_alter_ticket_query_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='number',
            field=ticket.models.PrefixedSerialNumberField(default=1, max_length=20, prefix='TKT/2022/', unique=True),
            preserve_default=False,
        ),
    ]