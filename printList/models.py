from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator
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
    print_Type = models.ForeignKey(PrintType, on_delete=models.CASCADE)
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

class MailSubjectLine(models.Model):
    subject_text = models.TextField()
    def __str__(self):
        return self.subject_text

    def save(self, *args, **kwargs):
        if not self.pk and MailSubjectLine.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Mail Message instance')
        return super(MailSubjectLine, self).save(*args, **kwargs)

class MailMessage(models.Model):
    message_text = models.TextField()
    def __str__(self):
        return self.message_text

    def save(self, *args, **kwargs):
        self.id = 1
        return super().save(*args, **kwargs)

class Print(models.Model):
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/{1}'.format(instance.net_ID_or_name, filename)

    intake_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    net_ID_or_name = models.CharField(max_length=10, null=True, validators=[RegexValidator(r'^[a-zA-Z]+$', 'Only letters in NetID/Name.')])
    email = models.EmailField(null=True)
    print_name = models.CharField(max_length=200)
    usage = models.PositiveSmallIntegerField(null=True, blank=True)
    file = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=['stl', '3mf', 'obj'])])
    printer_file = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=['gcode', 'form'])], null=True, blank=True)
    copies = models.PositiveSmallIntegerField()
    print_Type = models.ForeignKey(PrintType, on_delete=models.CASCADE)
    color = ChainedForeignKey(Color, chained_field="print_Type", chained_model_field="print_Type", show_all=False, auto_choose=True)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    resolution = ChainedForeignKey(Resolution, chained_field="print_Type", chained_model_field="print_Type", show_all=False, auto_choose=True, null=True, blank=True)
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


