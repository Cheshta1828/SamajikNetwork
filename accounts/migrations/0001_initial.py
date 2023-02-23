# Generated by Django 4.1.7 on 2023-02-23 13:39

import accounts.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, editable=False, max_length=200, null=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_email_verified', models.BooleanField(default=False, verbose_name='Email Verified')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='ngo_logos/')),
                ('address', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('website', models.URLField()),
                ('socials', models.CharField(max_length=500)),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('causes', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('animals', 'Animals'), ('arts_culture', 'Arts and Culture'), ('children', 'Children'), ('disaster_relief', 'Disaster Relief'), ('education', 'Education'), ('environment', 'Environment'), ('health', 'Health'), ('human_rights', 'Human Rights'), ('poverty', 'Poverty'), ('seniors', 'Seniors'), ('sports', 'Sports'), ('women', 'Women'), ('other', 'Other')], max_length=200, null=True)),
                ('no_of_employees', models.IntegerField()),
                ('achievements', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='volunteer_profile_images/')),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('interests', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('animals', 'Animals'), ('arts_culture', 'Arts and Culture'), ('children', 'Children'), ('disaster_relief', 'Disaster Relief'), ('education', 'Education'), ('environment', 'Environment'), ('health', 'Health'), ('human_rights', 'Human Rights'), ('poverty', 'Poverty'), ('seniors', 'Seniors'), ('sports', 'Sports'), ('women', 'Women'), ('other', 'Other')], max_length=200, null=True)),
                ('ngo_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('accounts.baseuser',),
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
    ]
