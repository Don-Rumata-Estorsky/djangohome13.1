# Generated by Django 5.1.3 on 2024-12-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='zapis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soderjanie', models.CharField(max_length=333)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
