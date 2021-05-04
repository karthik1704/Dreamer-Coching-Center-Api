# Generated by Django 3.1.7 on 2021-03-19 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_subject'),
        ('profiles', '0004_profile_tuition_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='classes.subject'),
            preserve_default=False,
        ),
    ]