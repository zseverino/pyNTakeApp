from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class PrintType(models.Model):
    type_text = models.CharField(max_length=10)
    def __str__(self):
        return self.type_text

class Printer(models.Model):
    printer_name = models.CharField(max_length=20)
    def __str__(self):
        return self.printer_name

class Color(models.Model):
    color_text = models.CharField(max_length=20)
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
    def __str__(self):
        return self.infill_text

class Purpose(models.Model):
    purpose_text = models.CharField(max_length=200)
    def __str__(self):
        return self.purpose_text

class Status(models.Model):
    status_text = models.CharField(max_length=20)
    def __str__(self):
        return self.status_text

class Print(models.Model):
    intake_datetime = models.DateField('Date')
    net_ID = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    print_name = models.CharField(max_length=200)
    usage = models.PositiveSmallIntegerField()
    file = models.FileField(upload_to="testFiles/", validators=[FileExtensionValidator(allowed_extensions=['3mf', 'gcode'])])
    copies = models.PositiveSmallIntegerField()
    print_Type = models.ForeignKey(PrintType, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    resolution = models.ForeignKey(Resolution, on_delete=models.CASCADE)
    infill = models.ForeignKey(Infill, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.print_name


