# Generated by Django 4.2.4 on 2023-09-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='post1.jpg', null=True, upload_to='avatars/'),
        ),
    ]