# Generated by Django 3.2.7 on 2021-09-23 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_alter_activeissue_assigned_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pullrequest',
            old_name='html_url',
            new_name='pr_link',
        ),
    ]
