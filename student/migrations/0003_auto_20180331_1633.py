# Generated by Django 2.0.2 on 2018-03-31 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180328_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourselist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.CourseOfferModel'),
        ),
    ]