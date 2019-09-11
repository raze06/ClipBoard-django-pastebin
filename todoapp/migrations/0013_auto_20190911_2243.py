# Generated by Django 2.0.9 on 2019-09-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0012_auto_20190911_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='lang',
            field=models.CharField(choices=[('text', 'Plain Text'), ('c', 'C'), ('cpp', 'C++'), ('csharp', 'C#'), ('java', 'Java'), ('js', 'JavaScript'), ('php', 'PHP'), ('py', 'Python'), ('sql', 'SQL')], default='c', max_length=10),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default='unknown', max_length=40),
        ),
    ]