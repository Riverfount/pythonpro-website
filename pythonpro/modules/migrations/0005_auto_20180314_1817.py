# Generated by Django 2.0.3 on 2018-03-14 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_section_module'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['module', 'order']},
        ),
        migrations.RemoveField(
            model_name='section',
            name='_module_slug',
        ),
    ]
