# Generated by Django 4.2.4 on 2023-09-07 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_likecomment_comment_alter_likepost_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likecomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='author',
        ),
    ]