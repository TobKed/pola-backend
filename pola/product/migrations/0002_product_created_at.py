import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(
                default=datetime.datetime(2015, 10, 25, 10, 59, 24, 358422, tzinfo=datetime.timezone.utc),
                auto_now_add=True,
            ),
            preserve_default=False,
        ),
    ]
