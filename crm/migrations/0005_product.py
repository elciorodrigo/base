# Generated by Django 2.2.1 on 2019-10-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_employeework_notecustomer_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=250, null=True)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('cod_in', models.CharField(blank=True, max_length=250, null=True)),
                ('ean', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]