# Generated by Django 4.0.2 on 2022-03-02 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=255)),
                ('batteryCapacity', models.CharField(max_length=255)),
                ('warrantyDuration', models.CharField(max_length=255)),
                ('warrantyType', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('screenSize', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ElectronicItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prices', models.FloatField(default=0)),
                ('description', models.CharField(max_length=255)),
                ('header', models.CharField(max_length=1023)),
                ('discount', models.FloatField(default=0)),
                ('electronic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.electronic')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('laptopType', models.CharField(max_length=255)),
                ('storageType', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
            ],
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('processorType', models.CharField(max_length=255)),
                ('storageCapacity', models.CharField(max_length=255)),
                ('mobileCableType', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
            ],
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('electronic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='electronic.electronic')),
                ('eReader', models.BooleanField(default=False)),
                ('storageCapacity', models.CharField(max_length=255)),
            ],
            bases=('electronic.electronic',),
        ),
        migrations.CreateModel(
            name='ElectronicItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=1023)),
                ('index', models.IntegerField()),
                ('electronicItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronic.electronicitem')),
            ],
        ),
    ]
