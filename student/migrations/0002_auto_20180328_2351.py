# Generated by Django 2.0.2 on 2018-03-28 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcourselist',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.CourseOfferModel'),
        ),
    ]
