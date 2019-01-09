# Generated by Django 2.0.9 on 2019-01-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20190102_0759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='to_do',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='td_no',
        ),
        migrations.AddField(
            model_name='todo',
            name='link_code',
            field=models.CharField(default='', max_length=8),
        ),
    ]