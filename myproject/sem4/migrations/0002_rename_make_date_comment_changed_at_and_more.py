# Generated by Django 4.2.4 on 2023-12-04 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sem4', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='make_date',
            new_name='changed_at',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='modify_date',
            new_name='created_at',
        ),
    ]
