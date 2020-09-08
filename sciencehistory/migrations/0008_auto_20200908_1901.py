# Generated by Django 3.1.1 on 2020-09-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciencehistory', '0007_historynode_significance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historynode',
            name='significance',
            field=models.IntegerField(choices=[(1, 'Lowest'), (2, 'Low'), (3, 'Moderate'), (4, 'High'), (5, 'Highest')], default=3),
        ),
    ]
