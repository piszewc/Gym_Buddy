# Generated by Django 2.1.7 on 2019-03-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0011_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]