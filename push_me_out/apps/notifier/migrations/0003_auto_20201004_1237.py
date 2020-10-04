# Generated by Django 3.1.1 on 2020-10-04 12:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0002_notificationstatemanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the notification type', max_length=64)),
                ('options', models.JSONField(default=dict, help_text='Extra options to be sent to the client')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='notificationstatemanager',
            name='notification_type',
            field=models.ForeignKey(help_text='Type of notification to be sent', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='notifier.notificationtype'),
        ),
    ]