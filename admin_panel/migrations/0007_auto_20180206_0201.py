# Generated by Django 2.0.2 on 2018-02-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_auto_20180203_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseoffermodel',
            name='capacity',
            field=models.IntegerField(default=40),
        ),
        migrations.AddField(
            model_name='courseoffermodel',
            name='section',
            field=models.CharField(blank=True, help_text='Example: A', max_length=1, null=True),
        ),
    ]
