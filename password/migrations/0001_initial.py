# Generated by Django 3.2.8 on 2021-10-06 21:35

from django.db import migrations, models
import password.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=90, null=True)),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(default=password.models.create_random_password, max_length=90)),
                ('note', models.TextField(null=True)),
            ],
        ),
    ]
