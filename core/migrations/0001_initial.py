# Generated by Django 3.2.12 on 2022-02-25 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('iso3', models.CharField(max_length=5)),
                ('iso2', models.CharField(max_length=5)),
                ('numeric_code', models.CharField(max_length=5)),
                ('phone_code', models.CharField(max_length=255)),
                ('capital', models.CharField(max_length=255)),
                ('currency', models.CharField(max_length=255)),
                ('currency_name', models.CharField(max_length=255)),
                ('currency_symbol', models.CharField(max_length=255)),
                ('tld', models.CharField(max_length=255)),
                ('native', models.CharField(max_length=255, null=True)),
                ('region', models.CharField(max_length=255)),
                ('subregion', models.CharField(max_length=255)),
                ('timezones', models.JSONField(default=list)),
                ('translations', models.JSONField(default=dict)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('emoji', models.CharField(max_length=191)),
                ('emojiU', models.CharField(max_length=191)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=5)),
                ('country_name', models.CharField(max_length=100)),
                ('state_code', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='core.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state_code', models.CharField(max_length=255)),
                ('state_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=5)),
                ('country_name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('wikiDataId', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='core.country')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='core.state')),
            ],
        ),
    ]