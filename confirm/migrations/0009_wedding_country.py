# Generated by Django 4.0.5 on 2022-06-20 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confirm', '0008_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='country',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to='confirm.country'),
        ),
    ]
