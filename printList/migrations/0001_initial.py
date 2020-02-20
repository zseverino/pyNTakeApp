# Generated by Django 3.0.3 on 2020-02-17 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assoc_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_text', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Infill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infill_text', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PrintType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_text', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_text', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intake_datetime', models.DateTimeField(verbose_name='Date')),
                ('net_ID', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('print_name', models.CharField(max_length=200)),
                ('usage', models.PositiveSmallIntegerField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('copies', models.PositiveSmallIntegerField()),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Association')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Color')),
                ('infill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Infill')),
                ('print_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.PrintType')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Printer')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Purpose')),
                ('resolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Resolution')),
            ],
        ),
    ]
