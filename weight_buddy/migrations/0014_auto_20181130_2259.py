# Generated by Django 2.1.3 on 2018-11-30 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weight_buddy', '0013_auto_20181130_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='exercise',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='weight_buddy.Exercises'),
        ),
    ]
