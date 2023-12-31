# Generated by Django 4.2.4 on 2023-09-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_comment_likecomment_post_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likeComment',
            field=models.ManyToManyField(null=True, related_name='comment_likes', to='catalog.likecomment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likePost',
            field=models.ManyToManyField(null=True, related_name='post_likes', to='catalog.likepost'),
        ),
    ]
