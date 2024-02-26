# Generated by Django 4.2.4 on 2024-02-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Internet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('simcard_class', models.CharField(choices=[('HamraheAval', 'HamraheAval'), ('Irancell', 'Irancell'), ('RighTel', 'RighTel')], max_length=20)),
                ('duration', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('simcard_type', models.CharField(max_length=50)),
            ],
        ),
    ]
