# Generated by Django 3.2.16 on 2023-02-02 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_alter_comment_comment_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='craft_categories',
            new_name='category',
        ),
    ]
