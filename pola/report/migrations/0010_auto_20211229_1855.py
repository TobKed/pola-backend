# Generated by Django 3.2.10 on 2021-12-29 17:55

import django.contrib.postgres.indexes
import django.utils.timezone
import model_utils.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_auto_20211003_0556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={
                'get_latest_by': 'created',
                'ordering': ['-created'],
                'permissions': (),
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
        migrations.RemoveIndex(
            model_name='report',
            name='report_repo_created_edcdde_brin',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='created_at',
            new_name='created',
        ),
        migrations.AddField(
            model_name='report',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now, editable=False, verbose_name='modified'
            ),
        ),
        migrations.AlterField(
            model_name='report',
            name='created',
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now, editable=False, verbose_name='created'
            ),
        ),
        migrations.AddIndex(
            model_name='report',
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=['created'], name='report_repo_created_d51aaf_brin', pages_per_range=16
            ),
        ),
    ]