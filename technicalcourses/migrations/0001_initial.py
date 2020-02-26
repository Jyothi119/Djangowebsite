# Generated by Django 3.0.3 on 2020-02-20 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allcourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=200)),
                ('insname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp', models.CharField(max_length=500)),
                ('il', models.CharField(max_length=500)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technicalcourses.allcourses')),
            ],
        ),
    ]
