# Generated by Django 2.2.1 on 2020-02-10 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_auto_20200210_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='person_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Pessoa Fisica'), (2, 'Pessoa Juridica')], null=True),
        ),
    ]