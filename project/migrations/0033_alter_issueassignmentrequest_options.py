# Generated by Django 3.2.7 on 2021-10-11 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0032_alter_issueassignmentrequest_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issueassignmentrequest',
            options={'ordering': ['-state', 'created_on']},
        ),
    ]
