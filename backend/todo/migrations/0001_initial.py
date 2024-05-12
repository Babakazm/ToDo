# Generated by Django 5.0.1 on 2024-05-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('deadline', models.DateField()),
            ],
        ),
    ]
