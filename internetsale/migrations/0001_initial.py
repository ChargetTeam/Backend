# Generated by Django 4.2.4 on 2024-02-26 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('internet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternetSale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('internet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internet.internet')),
            ],
        ),
    ]