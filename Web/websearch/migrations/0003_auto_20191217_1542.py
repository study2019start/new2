# Generated by Django 2.0.4 on 2019-12-17 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websearch', '0002_auto_20191217_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_classinfo',
            name='fid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='websearch.First_class'),
        ),
    ]
