# Generated by Django 4.1.6 on 2023-03-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_alter_topic_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='pic',
            field=models.ImageField(upload_to='vote/%y/%m'),
        ),
    ]
