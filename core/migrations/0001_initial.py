# Generated by Django 4.0.6 on 2022-09-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.EmailField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
