# Generated by Django 3.2.12 on 2022-03-24 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220324_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='core.country'),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='core.state'),
        ),
    ]