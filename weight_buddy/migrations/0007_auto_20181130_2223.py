# Generated by Django 2.1.3 on 2018-11-30 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0006_auto_20181130_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='excercises',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='weight_buddy.Exercise'),
        ),
    ]