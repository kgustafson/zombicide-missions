# Generated by Django 3.1.3 on 2020-11-15 19:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=100)),
                ('pdf_loc', models.CharField(max_length=100)),
                ('title_id', models.CharField(max_length=100)),
                ('num_players', models.CharField(max_length=100)),
                ('length_play', models.CharField(max_length=100)),
                ('num_tiles', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
