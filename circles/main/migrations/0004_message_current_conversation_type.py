# Generated by Django 4.2.4 on 2023-09-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_conversation_parent_circle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='current_conversation_type',
            field=models.CharField(default='normal', max_length=16),
        ),
    ]
