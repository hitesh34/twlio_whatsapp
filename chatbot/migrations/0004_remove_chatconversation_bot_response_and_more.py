# Generated by Django 4.0.5 on 2023-09-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_rename_response_chatconversation_bot_response_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatconversation',
            name='bot_response',
        ),
        migrations.RemoveField(
            model_name='chatconversation',
            name='user_response',
        ),
        migrations.AddField(
            model_name='chatconversation',
            name='messages',
            field=models.TextField(default='Welcome to HomeOpen'),
        ),
        migrations.AddField(
            model_name='chatconversation',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
