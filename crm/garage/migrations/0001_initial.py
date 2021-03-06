# Generated by Django 4.0 on 2022-01-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('ph_no', models.IntegerField()),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
    ]
