# Generated by Django 3.1 on 2020-08-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]