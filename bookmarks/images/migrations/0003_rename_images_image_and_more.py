# Generated by Django 4.1.4 on 2022-12-28 09:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0002_rename_user_like_images_users_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameIndex(
            model_name='image',
            new_name='images_imag_created_d57897_idx',
            old_name='images_imag_created_b41a97_idx',
        ),
    ]
