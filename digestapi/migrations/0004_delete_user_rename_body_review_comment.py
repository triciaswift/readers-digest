# Generated by Django 4.2.7 on 2023-11-03 19:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("digestapi", "0003_alter_bookcategory_timestamp_alter_review_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="body",
            new_name="comment",
        ),
    ]