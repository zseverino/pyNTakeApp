# Generated by Django 3.0.7 on 2020-06-26 03:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import printList.models
import smart_selects.db_fields


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
                ('res_text', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer_name', models.CharField(max_length=20)),
                ('print_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.PrintType')),
            ],
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intake_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('net_ID_or_name', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('print_name', models.CharField(max_length=200)),
                ('usage', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('file', models.FileField(upload_to=printList.models.Print.user_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['stl', '3mf', 'gcode'])])),
                ('copies', models.PositiveSmallIntegerField()),
                ('status', models.CharField(choices=[('NOTPRINTED', 'Not Printed'), ('PRINTING', 'Printing'), ('PRINTED', 'Printed')], default='Not Printed', max_length=11)),
                ('verification', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Association')),
                ('color', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='print_Type', chained_model_field='print_Type', on_delete=django.db.models.deletion.CASCADE, to='printList.Color')),
                ('infill', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='print_Type', chained_model_field='print_Type', null=True, on_delete=django.db.models.deletion.CASCADE, to='printList.Infill')),
                ('print_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.PrintType')),
                ('printer', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='print_Type', chained_model_field='print_Type', null=True, on_delete=django.db.models.deletion.CASCADE, to='printList.Printer')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.Purpose')),
                ('resolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='printList.Resolution')),
            ],
        ),
        migrations.AddField(
            model_name='infill',
            name='print_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.PrintType'),
        ),
        migrations.AddField(
            model_name='color',
            name='print_Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printList.PrintType'),
        ),
    ]
