# Generated by Django 4.2.1 on 2023-06-15 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_rename_category_category_name_remove_bid_user_bid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]