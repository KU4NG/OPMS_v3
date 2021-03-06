# Generated by Django 2.0.6 on 2018-08-03 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('platform_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platforminfo',
            name='add_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pl_user', to=settings.AUTH_USER_MODEL, verbose_name='添加人'),
        ),
        migrations.AddField(
            model_name='platforminfo',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='公开'),
        ),
        migrations.AlterField(
            model_name='platforminfo',
            name='belong',
            field=models.PositiveSmallIntegerField(choices=[(1, '公司平台'), (2, '运维平台'), (3, '其它平台')], verbose_name='隶属'),
        ),
    ]
