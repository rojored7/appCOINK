# Generated by Django 4.1 on 2022-08-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=100)),
                ('emai', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
    ]
