# Generated by Django 4.1.7 on 2023-02-24 19:56

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_volunteer_interests_baseuser_interests_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Last Name')),
                ('age', models.IntegerField(blank=True, max_length=255, null=True, verbose_name='Age')),
                ('bio', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'NGOs',
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='ngomodel',
            options={'verbose_name_plural': 'NGOs'},
        ),
        migrations.AlterField(
            model_name='baseuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]