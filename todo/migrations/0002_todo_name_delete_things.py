# Generated by Django 4.1.6 on 2023-03-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Things',
        ),
    ]