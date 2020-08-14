# Generated by Django 3.1 on 2020-08-14 06:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('message_html', models.TextField(editable=False)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='posts', to='groups.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts',
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-create_at'],
                'unique_together': {('user', 'group')},
            },
        ),
    ]
