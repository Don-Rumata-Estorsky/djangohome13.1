# Generated by Django 5.1.3 on 2024-12-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('slug', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='films',
        ),
    ]
