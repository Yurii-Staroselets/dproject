# Generated by Django 3.1.7 on 2022-06-04 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_line',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_line2',
            new_name='post_office',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='postcode',
            new_name='region',
        ),
        migrations.RemoveField(
            model_name='address',
            name='town_city',
        ),
    ]
