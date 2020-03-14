# Generated by Django 3.0.4 on 2020-03-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciencehistory', '0002_historynode_modified_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferringFlow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.PositiveIntegerField(default=0)),
                ('end', models.PositiveIntegerField(default=0)),
                ('indirect', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='historynode',
            name='link',
            field=models.CharField(default='http://stic.dothome.co.kr/w/', max_length=100),
        ),
    ]