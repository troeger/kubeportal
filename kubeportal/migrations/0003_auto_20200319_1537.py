# Generated by Django 2.2.10 on 2020-03-19 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0026_client_multiple_response_types'),
        ('kubeportal', '0002_auto_20200224_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name for the user group')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Members of the user group')),
            ],
        ),
        migrations.CreateModel(
            name='OidcClient',
            fields=[
                ('client_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='oidc_provider.Client')),
            ],
            bases=('oidc_provider.client',),
        ),
        migrations.RenameModel(
            old_name='Link',
            new_name='WebApplication'
        ),
        migrations.AlterModelOptions(
            name='WebApplication',
            options={'verbose_name': 'web application'},
        ),
        migrations.RenameField(
            model_name='WebApplication',
            old_name='name',
            new_name='link_name'
        ),
        migrations.RenameField(
            model_name='WebApplication',
            old_name='url',
            new_name='link_url'
        ),
        migrations.AlterField(
            model_name='webapplication',
            name='link_name',
            field=models.CharField(blank=True, help_text="You can use the placeholders '{{namespace}}' and '{{serviceaccount}}' in the title.", max_length=100, null=True, verbose_name='Link title'),
        ),
        migrations.AlterField(
            model_name='webapplication',
            name='link_url',
            field=models.URLField(blank=True, help_text="You can use the placeholders '{{namespace}}' and '{{serviceaccount}}' in the URL.", null=True, verbose_name='Link URL'),
        ),
        migrations.AddField(
            model_name='WebApplication',
            name='link_show',
            field=models.BooleanField(default=False, verbose_name='Show link on welcome page')
        ),
        migrations.AddField(
            model_name='WebApplication',
            name='name',
            field=models.CharField(max_length=100)
        ),
        migrations.AddField(
            model_name='WebApplication',
            name='oidc_enable',
            field=models.BooleanField(default=False, verbose_name='Enable OIDC authentication')
        ),
        migrations.AddField(
            model_name='WebApplication',
            name='oidc_client_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Client ID')
        ),
        migrations.AddField(
            model_name='WebApplication',
            name='oidc_client_secret',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Client secret')
        ),
        migrations.AddField(
            model_name='WebApplication',
            name='_oidc_redirect_uris',
            field=models.TextField(blank=True, default='', help_text='Enter each URI on a new line.', null=True, verbose_name='Allowed redirects after login')
        ),
        migrations.AddField(
            model_name='oidcclient',
            name='web_application',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kubeportal.WebApplication'),
        ),
        migrations.AddField(
            model_name='group',
            name='web_applications',
            field=models.ManyToManyField(to='kubeportal.WebApplication', verbose_name='Web applications enabled for this user group'),
        ),
    ]
