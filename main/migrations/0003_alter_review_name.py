# Generated by Django 4.1 on 2022-08-23 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
        ),
    ]
