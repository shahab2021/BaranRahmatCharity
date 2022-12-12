# Generated by Django 4.0.6 on 2022-07-21 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_hesabmoaseseh_options_alter_khayer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='khayer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='management.khayer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='sandogh_khayerieh',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='management.sandoghkhayerieh'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='tahvilgirandeh_sandogh',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='management.tahvilgirandehsandogh'),
        ),
    ]
