# Generated by Django 2.2.10 on 2020-03-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeportal', '0003_auto_20200326_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='portalgroup',
            name='auto_admin',
            field=models.BooleanField(default=False, verbose_name='Users in this group are admins'),
        ),
        migrations.AddField(
            model_name='portalgroup',
            name='subauth',
            field=models.BooleanField(default=False, help_text='Enable sub-authentication with Kubernetes Bearer token.', verbose_name='Enable sub-authentication'),
        ),
    ]