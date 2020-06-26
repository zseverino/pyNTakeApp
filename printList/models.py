from django.db import models
from django.core.validators import FileExtensionValidator
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class PrintType(models.Model):
    type_text = models.CharField(max_length=10)
    def __str__(self):
        return self.type_text

class Printer(models.Model):
    printer_name = models.CharField(max_length=20)
    print_Type = models.ForeignKey(PrintType, on_delete=models.CASCADE)
    def __str__(self):
        return self.printer_name

class Color(models.Model):
    color_text = models.CharField(max_length=20)
    print_Type = models.ForeignKey(PrintType,  on_delete=models.CASCADE)
    def __str__(self):
        return self.color_text

class Association(models.Model):
    assoc_text = models.CharField(max_length=200)
    def __str__(self):
        return self.assoc_text

class Resolution(models.Model):
    res_text = models.CharField(max_length=10)
    def __str__(self):
        return self.res_text

class Infill(models.Model):
    infill_text = models.CharField(max_length=10)
    print_Type = models.ForeignKey(PrintType, on_delete=models.CASCADE)
    def __str__(self):
        return self.infill_text

class Purpose(models.Model):
    purpose_text = models.CharField(max_length=200)
    def __str__(self):
        return self.purpose_text

class Print(models.Model):
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/{1}'.format(instance.net_ID_or_name, filename)

    intake_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    net_ID_or_name = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    print_name = models.CharField(max_length=200)
    usage = models.PositiveSmallIntegerField(null=True, blank=True)
    file = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=['stl', '3mf', 'gcode'])])
    copies = models.PositiveSmallIntegerField()
    print_Type = models.ForeignKey(PrintType, on_delete=models.CASCADE)
    color = ChainedForeignKey(Color, chained_field="print_Type", chained_model_field="print_Type", show_all=False, auto_choose=True)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE, null=True, blank=True)
    infill = ChainedForeignKey(Infill, chained_field="print_Type", chained_model_field="print_Type", show_all=False, auto_choose=True, null=True, blank=True)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    printer = ChainedForeignKey(Printer, chained_field="print_Type", chained_model_field="print_Type", show_all=False, auto_choose=True, null=True, blank=True)

    STATUS_CHOICES = (
        ('NOTPRINTED', 'Not Printed'),
        ('PRINTING', 'Printing'),
        ('PRINTED', 'Printed'),
    )
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default="Not Printed")
    verification = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.print_name


