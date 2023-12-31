# Generated by Django 4.2.4 on 2023-09-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_likecomment_comment_alter_likepost_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likecomment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='likepost',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='likePost',
            field=models.ManyToManyField(related_name='post_likes', to='catalog.likepost'),
        ),
    ]
