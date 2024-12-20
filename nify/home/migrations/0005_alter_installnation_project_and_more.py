# Generated by Django 5.1.4 on 2024-12-19 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_installnation_project_alter_requirements_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installnation',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='installnation', to='home.project'),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='home.project'),
        ),
    ]
