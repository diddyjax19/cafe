# Generated by Django 3.2.16 on 2023-02-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_alter_post_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(verbose_name='Comments'),
        ),
    ]
