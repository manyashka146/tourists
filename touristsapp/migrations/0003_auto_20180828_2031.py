# Generated by Django 2.1 on 2018-08-28 20:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('touristsapp', '0002_auto_20180828_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='visit',
            name='location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='touristsapp.Location'),
        ),
        migrations.AddField(
            model_name='visit',
            name='ratio',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='visit',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='visits', to=settings.AUTH_USER_MODEL),
        ),
    ]
