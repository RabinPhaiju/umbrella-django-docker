# Generated by Django 3.2.6 on 2022-01-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]