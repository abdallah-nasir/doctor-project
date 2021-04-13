# Generated by Django 3.1.3 on 2021-04-13 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0011_auto_20210413_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='Date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='reservation',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
