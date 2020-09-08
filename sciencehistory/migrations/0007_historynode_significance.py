# Generated by Django 3.1.1 on 2020-09-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciencehistory', '0006_auto_20200315_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='historynode',
            name='significance',
            field=models.CharField(choices=[('L2', 'Lowest'), ('L1', 'Low'), ('M0', 'Moderate'), ('H1', 'High'), ('H2', 'Highest')], default='M0', max_length=2),
        ),
    ]