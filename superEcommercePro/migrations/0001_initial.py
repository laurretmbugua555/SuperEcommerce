# Generated by Django 4.2.3 on 2023-07-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qqty', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=35)),
            ],
        ),
    ]