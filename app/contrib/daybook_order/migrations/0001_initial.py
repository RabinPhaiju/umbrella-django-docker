# Generated by Django 3.2.6 on 2022-02-10 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('daybook_line', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daybook_order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('s_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('daybook_line', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='daybook_line.daybook_line')),
            ],
        ),
    ]
