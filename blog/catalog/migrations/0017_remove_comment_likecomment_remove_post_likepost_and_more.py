# Generated by Django 4.2.4 on 2023-09-07 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_remove_likecomment_comment_remove_likepost_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likeComment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likePost',
        ),
        migrations.AddField(
            model_name='likecomment',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.comment'),
        ),
        migrations.AddField(
            model_name='likepost',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.post'),
        ),
    ]