# Generated by Django 3.1.7 on 2021-03-27 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='tuition_class',
            field=models.ForeignKey(limit_choices_to={'tuititonclass_id': 'self'}, on_delete=django.db.models.deletion.CASCADE, to='classes.tuitionclass'),
        ),
    ]
