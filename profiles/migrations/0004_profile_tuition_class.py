# Generated by Django 3.1.7 on 2021-03-18 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('profiles', '0003_auto_20210317_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tuition_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='classes.tuitionclass'),
            preserve_default=False,
        ),
    ]
