# Generated by Django 5.0.2 on 2024-03-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_rename_number_bills_bill_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
