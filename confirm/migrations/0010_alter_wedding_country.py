# Generated by Django 4.0.5 on 2022-06-20 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0009_wedding_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wedding',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='confirm.country'),
        ),
    ]
