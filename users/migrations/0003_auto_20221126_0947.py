# Generated by Django 3.2.16 on 2022-11-26 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_templates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Templates',
            new_name='Template',
        ),
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ['user'], 'verbose_name': 'Шаблон', 'verbose_name_plural': 'Шаблоны'},
        ),
    ]