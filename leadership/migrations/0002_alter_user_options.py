# Generated by Django 3.2.4 on 2021-11-16 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leadership', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('is_student', 'Can view student app'), ('is_trainer', 'Can view trainer app'), ('is_leader', 'Can view leader app')), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
