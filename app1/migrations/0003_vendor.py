# Generated by Django 3.2.11 on 2024-10-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_cart_totalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.CharField(max_length=10)),
                ('add', models.TextField()),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
