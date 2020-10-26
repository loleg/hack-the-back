# Generated by Django 3.1.2 on 2020-10-26 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HackathonApplicant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('AP', 'Applied'), ('UR', 'Under Review'), ('AC', 'Accepted')], default='AP', max_length=2)),
                ('gender', models.CharField(choices=[('MA', 'Male'), ('FM', 'Female'), ('PS', 'Prefer not to say')], default='PS', max_length=2)),
                ('school', models.CharField(max_length=256)),
                ('year_of_graduation', models.CharField(max_length=4)),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='hackathon.hackathon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
