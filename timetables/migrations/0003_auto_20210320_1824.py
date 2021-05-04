# Generated by Django 3.1.7 on 2021-03-20 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_subject'),
        ('timetables', '0002_period_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='subject',
        ),
        migrations.AddField(
            model_name='period',
            name='name',
            field=models.TextField(choices=[('Study', 'Study'), ('Test', 'Test'), ('SPL', 'SPL')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timetable',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classes.subject'),
            preserve_default=False,
        ),
    ]